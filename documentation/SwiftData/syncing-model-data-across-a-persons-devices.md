# Syncing model data across a person’s devices

**Framework**: SwiftData

Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app’s model data using iCloud.

#### Overview

People who use your app to create content expect that content to be available on all of their devices. SwiftData makes it possible to synchronize content by abstracting away the associated complexities. To adopt the framework’s automatic sync functionality, add two Xcode capabilities to your app. The system operates with a set of predictable behaviors, such as using your app’s `Entitlements.plist` file to infer the CloudKit configuration.

SwiftData uses the [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer) class from Core Data to handle CloudKit synchronization. For more information about how your models become instances of [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord), see [`Reading CloudKit Records for Core Data`](https://developer.apple.com/documentation/CoreData/reading-cloudkit-records-for-core-data).

##### Add the Icloud and Background Modes Capabilities

SwiftData requires two separate capabilities to perform automatic iCloud sync: the iCloud capability, which lets you configure CloudKit, and the Background Modes capability, which lets your app receive remote notifications from CloudKit that contain information about new changes on the server.

> ❗ **Important**: The iCloud capability requires an active Apple Developer account with admin permissions.

The iCloud capability requires an active Apple Developer account with admin permissions.

To add the iCloud and Background Modes capabilities:

1. Follow the steps in [`Configuring iCloud services`](https://developer.apple.com/documentation/Xcode/configuring-icloud-services) to add the iCloud capability to your Xcode project, enable CloudKit, and create or choose an existing  — an object that CloudKit uses to isolate your app’s databases on the iCloud servers and manage their access and operations.
2. Follow the steps in [`Configuring background execution modes`](https://developer.apple.com/documentation/Xcode/configuring-background-execution-modes) to add the Background Modes capability, enabling the Remote notifications option. The system delivers remote notifications silently to your app, allowing SwiftData to process the changes they describe and keep your local model data in sync with the iCloud servers.

##### Define a Cloudkit Compatible Schema

A model layer described using macros in SwiftData will, in many cases, generate a schema already compatible with CloudKit. However, the SwiftData framework does include a small number of features that CloudKit doesn’t support natively, such as unique constraints and nonoptional relationships. It’s important you consider these limitations as you design your app’s model layer (or adapt an existing one) to ensure it remains compatible with CloudKit.

| SwiftData macro | CloudKit schema limitation |
| --- | --- |
| `@Attribute` | The framework synchronizes changes concurrently and at opportune times, which means CloudKit is unable to enforce the [`unique`](schema/attribute/option/unique.md) property option. |
| `@Relationship` | The iCloud servers don’t guarantee atomic processing of relationship changes, so CloudKit requires all relationships to be optional. SwiftData automatically sets the inverse of a relationship if it can reliably infer that inverse from your schema. Otherwise, explicitly set the inverse before saving because CloudKit processes changes in an indeterminate order. The framework doesn’t immediately synchronize changes, meaning CloudKit is unable to support the [`Schema.Relationship.DeleteRule.deny`](schema/relationship/deleterule-swift.enum/deny.md) delete rule. |

You manually initialize your app’s CloudKit schema during development — as the following section describes — but you need to promote that schema to production before releasing your app. CloudKit schemas are additive only, which means you’re unable to delete model types or change existing model attributes after you promote a schema to production.

##### Initialize the Cloudkit Development Schema

After you define a model layer that’s compatible with CloudKit, use the existing integration from Core Data with CloudKit to initialize a copy of that model layer on the iCloud servers. For example, you might do this during app launch by adding the necessary code to the `init()` function of the type in your app that adopts the [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol from SwiftUI.

Follow these steps to ensure proper CloudKit schema initialization:

1. Create an instance of [`ModelConfiguration`](modelconfiguration.md), which provides some basic information about the app’s SwiftData stack.
2. Use the configuration’s [`url`](modelconfiguration/url.md) property to create an instance of [`NSPersistentStoreDescription`](https://developer.apple.com/documentation/CoreData/NSPersistentStoreDescription), enabling SwiftData and Core Data to reference the same store on disk.
3. Configure the store description with your app’s CloudKit container identifier.
4. Request Core Data load the store synchronously, to guarantee that the load finishes before you attempt to initialize the CloudKit schema.
5. Create a managed object model that contains the same model types as the `ModelConfiguration` instance.
6. Use [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer) to load the store from the description and to initialize the CloudKit schema.
7. Unload the persistent store before creating an instance of [`ModelContainer`](modelcontainer.md) to avoid both frameworks attempting to sync data to CloudKit.

```swift
let config = ModelConfiguration()

do {
#if DEBUG
    // Use an autorelease pool to make sure Swift deallocates the persistent 
    // container before setting up the SwiftData stack.
    try autoreleasepool {
        let desc = NSPersistentStoreDescription(url: config.url)
        let opts = NSPersistentCloudKitContainerOptions(containerIdentifier: "iCloud.com.example.Trips")
        desc.cloudKitContainerOptions = opts
        // Load the store synchronously so it completes before initializing the 
        // CloudKit schema.
        desc.shouldAddStoreAsynchronously = false
        if let mom = NSManagedObjectModel.makeManagedObjectModel(for: [Trip.self, Accommodation.self]) {
            let container = NSPersistentCloudKitContainer(name: "Trips", managedObjectModel: mom)
            container.persistentStoreDescriptions = [desc]
            container.loadPersistentStores {_, err in
                if let err {
                    fatalError(err.localizedDescription)
                }
            }
            // Initialize the CloudKit schema after the store finishes loading.
            try container.initializeCloudKitSchema()
            // Remove and unload the store from the persistent container.
            if let store = container.persistentStoreCoordinator.persistentStores.first {
                try container.persistentStoreCoordinator.remove(store)
            }
        }
    }
#endif
    modelContainer = try ModelContainer(for: Trip.self, Accommodation.self,
                                        configurations: config)
} catch {
    fatalError(error.localizedDescription)
}
```

To ensure that schema initialization runs only in nonproduction builds, wrap your code with the `#if` compiler directive and specify the `DEBUG` compiler flag.

Go to the [`CloudKit Console`](https://developer.apple.comhttps://icloud.developer.apple.com) to verify the initialized schema. If you’re unable to see your schema’s record types or data, you may need to enable querying support. For more information, see [`Inspecting and Editing an iCloud Container’s Schema`](https://developer.apple.com/documentation/CloudKit/inspecting-and-editing-an-icloud-container-s-schema).

##### Configure Swiftdata to Use an Existing Cloudkit Container

By default, SwiftData inspects your app’s `Entitlements.plist` file to determine which CloudKit container to use, and selects the first identifier it finds in that file. If your app uses multiple CloudKit containers, you may need to configure SwiftData to use a specific identifier instead of relying on the default behavior.

> ❗ **Important**: For apps already using a production CloudKit schema, specify only containers that SwiftData or Core Data have managed previously. All other CloudKit containers are incompatible.

For apps already using a production CloudKit schema, specify only containers that SwiftData or Core Data have managed previously. All other CloudKit containers are incompatible.

To opt out of automatic container discovery in SwiftData, create an instance of [`ModelConfiguration`](modelconfiguration.md) and use the initializer’s `cloudKitDatabase` parameter to specify your preferred identifier:

```swift
let config = ModelConfiguration(cloudKitDatabase: .private("iCloud.com.example.Trips"))
let modelContainer = try ModelContainer(for: Trip.self, Accommodation.self,
                                        configurations: config)
```

##### Disable Automatic Sync in Apps Already Using Cloudkit

SwiftData uses CloudKit to provide automatic iCloud sync and therefore requires the same Xcode-managed capabilities as those found in traditional CloudKit apps. This sharing of capabilities may lead to issues in apps already using CloudKit, because SwiftData assumes the presence of those capabilities as an indication that it handles sync. For example, automatic sync isn’t possible if there are incompatibilities between a SwiftData schema and an existing CloudKit schema.

In such scenarios, opt out of automatic iCloud sync by creating an instance of [`ModelConfiguration`](modelconfiguration.md) and explicitly pass [`none`](modelconfiguration/cloudkitdatabase-swift.struct/none.md) for the `cloudKitDatabase` parameter:

```swift
let config = ModelConfiguration(cloudKitDatabase: .none)
let modelContainer = try ModelContainer(for: Trip.self, Accommodation.self,
                                        configurations: config)
```

Specifying `none` overrides any automatically discovered identifiers and disables SwiftData’s automatic iCloud sync.

## See Also

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)
  Describe your model classes to SwiftData using the framework’s macros, and store instances of those models so they exist beyond the app’s runtime.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [Adopting SwiftData for a Core Data app](../CoreData/adopting-swiftdata-for-a-core-data-app.md)
  Persist data in your app intuitively with the Swift native persistence framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices)*