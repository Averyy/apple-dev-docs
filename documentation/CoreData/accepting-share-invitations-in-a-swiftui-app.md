# Accepting Share Invitations in a SwiftUI App

**Framework**: Core Data

Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.

#### Overview

When the user accepts an invitation to participate in a CloudKit share, the system passes that share’s metadata to your app’s scene delegate for processing. To receive this metadata in a SwiftUI app:

1. Add a scene delegate — an object that conforms to [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate) — that’s responsible for passing the accepted share metadata to your app’s persistent container.
2. Add an application delegate — an object that conforms to [`UIApplicationDelegate`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate) — that configures new scenes to use your custom scene delegate class.
3. Modify your app’s [`App`](https://developer.apple.com/documentation/SwiftUI/App) structure to use [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/SwiftUI/UIApplicationDelegateAdaptor) to initialize and manage an application delegate at runtime.

##### Add a Scene Delegate to Process Share Invitations

In response to the user accepting a CloudKit share invitation, the system routes that action, for processing, to the delegate of the app’s active scene. SwiftUI apps don’t contain a scene delegate by default, but you can add one, and use it to implement the [`windowScene(_:userDidAcceptCloudKitShareWith:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:userDidAcceptCloudKitShareWith:)) method. Your implementation is responsible for passing the provided share metadata to your app’s persistent container for processing.

To create the scene delegate, right-click your project in Xcode’s Project navigator and select New File. Choose the Swift File template and name the file `SceneDelegate.swift`. Open the new file in Xcode’s source editor and define the `SceneDelegate` class as a subclass of [`UIResponder`](https://developer.apple.com/documentation/UIKit/UIResponder) that adopts the [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate) protocol. Within this class, add your implementation of [`windowScene(_:userDidAcceptCloudKitShareWith:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:userDidAcceptCloudKitShareWith:)), as shown in the following example.

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    func windowScene(_ windowScene: UIWindowScene,
        userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShare.Metadata) {
        
        let stack = CoreDataStack.shared

        // Get references to the app's persistent container 
        // and shared persistent store.
        let container = stack.persistentContainer
        let store = stack.sharedPersistentStore

        // Tell the container to accept the specified share, adding
        // the shared objects to the shared persistent store.
       container.acceptShareInvitations(from: [cloudKitShareMetadata],
                                        into: store,
                                        completion: nil)
    }
}
```

The example above uses a `CoreDataStack` object that manages the initialization of the persistent container, and the private and shared persistent stores. For a reference implementation, see the sample code project [`Synchronizing a local store to the cloud`](synchronizing-a-local-store-to-the-cloud.md).

##### Add an Application Delegate to Configure New Scenes

Before an app connects a new scene, the system asks the application delegate to provide the configuration for the new scene, including the class to use as its own delegate. By providing this configuration, your app can use your custom delegate implementation and correctly process accepted CloudKit share invitations. Because SwiftUI apps don’t include an application delegate, you need to add one to your app’s target.

Right-click your project in Xcode’s Project navigator and select New File. Choose the Swift File template and name the file `AppDelegate.swift`. Open the new file in Xcode’s source editor and add the following code, which configures each new scene to use the custom `SceneDelegate` class from the previous section.

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, configurationForConnecting
        connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions) -> UISceneConfiguration {

        // Create a scene configuration object for the
        // specified session role.
        let config = UISceneConfiguration(name: nil,
            sessionRole: connectingSceneSession.role)

        // Set the configuration's delegate class to the
        // scene delegate that implements the share
        // acceptance method.
        config.delegateClass = SceneDelegate.self

        return config
    }
}
```

For more information on scene configuration, see [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)).

##### Modify Your App to Utilize the Application Delegate

After you add the scene and application delegates to your app’s target, use the [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/SwiftUI/UIApplicationDelegateAdaptor) property wrapper to instruct your app’s top-level object — the structure that adopts SwiftUI’s [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol — to initialize and manage an instance of the application delegate at runtime, as shown in the following example.

```swift
@main
struct SharingExample: App {
    // Instruct SwiftUI to use the custom AppDelegate class 
    // as the app's application delegate.
    @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext,
                    CoreDataStack.shared.persistentContainer.viewContext)
        }
    }
}
```

With this change in place, whenever the user accepts a CloudKit share invitation, SwiftUI notifies the active scene’s delegate where you can process the accepted invitation accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/accepting-share-invitations-in-a-swiftui-app)*