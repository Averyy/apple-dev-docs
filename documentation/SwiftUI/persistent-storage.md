# Persistent storage

**Framework**: SwiftUI

Store data for use across sessions of your app.

#### Overview

The operating system provides ways to store data when your app closes, so that when people open your app again later, they can continue working without interruption. The mechanism that you use depends on factors like what and how much you need to store, whether you need serialized or random access to the data, and so on.

![None](https://docs-assets.developer.apple.com/published/45f566a52f46e696909b2586bde96bd8/persistent-storage-hero%402x.png)

You use the same kinds of storage in a SwiftUI app that you use in any other app. For example, you can access files on disk using the [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) interface. However, SwiftUI also provides conveniences that make it easier to use certain kinds of persistent storage in a declarative environment. For example, you can use [`FetchRequest`](fetchrequest.md) and [`FetchedResults`](fetchedresults.md) to interact with a Core Data model.

## Topics

### Saving state across app launches
- [Restoring your app’s state with SwiftUI](restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [func defaultAppStorage(UserDefaults) -> some View](view/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [struct AppStorage](appstorage.md)
  A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.
- [struct SceneStorage](scenestorage.md)
  A property wrapper type that reads and writes to persisted, per-scene storage.
### Accessing Core Data
- [Loading and displaying a large data feed](loading-and-displaying-a-large-data-feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [var managedObjectContext: NSManagedObjectContext](environmentvalues/managedobjectcontext.md)
- [struct FetchRequest](fetchrequest.md)
  A property wrapper type that retrieves entities from a Core Data persistent store.
- [struct FetchedResults](fetchedresults.md)
  A collection of results retrieved from a Core Data store.
- [struct SectionedFetchRequest](sectionedfetchrequest.md)
  A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [struct SectionedFetchResults](sectionedfetchresults.md)
  A collection of results retrieved from a Core Data persistent store, grouped into sections.

## See Also

- [Model data](model-data.md)
  Manage the data that your app uses to drive its interface.
- [Environment values](environment-values.md)
  Share data throughout a view hierarchy using the environment.
- [Preferences](preferences.md)
  Indicate configuration preferences from views to their container views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/persistent-storage)*