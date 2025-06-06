# Core Data

**Framework**: Core Data  
**Kind**: module

Persist or cache data on a single device, or sync data to multiple devices with CloudKit.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Use Core Data to save your application’s permanent data for offline use, to cache temporary data, and to add undo functionality to your app on a single device. To sync data across multiple devices in a single iCloud account, Core Data automatically mirrors your schema to a CloudKit container.

Through Core Data’s Data Model editor, you define your data’s types and relationships, and generate respective class definitions. Core Data can then manage object instances at runtime to provide the following features.

##### Persistence

Core Data abstracts the details of mapping your objects to a store, making it easy to save data from Swift and Objective-C without administering a database directly.

![Flow diagram showing an app saving data to and loading data from a persistent store.](https://docs-assets.developer.apple.com/published/75428f775be2ff5c6fe139221ff330d4/media-3119932%402x.png)

##### Undo and Redo of Individual and Batched Changes

Core Data’s undo manager tracks changes and can roll them back individually, in groups, or all at once, making it easy to add undo and redo support to your app.

![Figure showing a shake to undo gesture causing an element to be removed from a list.](https://docs-assets.developer.apple.com/published/640964de6db0e195490edb69b0d5aae8/media-3118362%402x.png)

##### Background Data Tasks

Perform potentially UI-blocking data tasks, like parsing JSON into objects, in the background. You can then cache or store the results to reduce server roundtrips.

![Flow diagram showing data from an endpoint populating objects in the background before updating the UI.](https://docs-assets.developer.apple.com/published/d71b242e7299eb1f75bd78763df7278c/media-3118359%402x.png)

##### View Synchronization

Core Data also helps keep your views and data synchronized by providing data sources for table and collection views.

##### Versioning and Migration

Core Data includes mechanisms for versioning your data model and migrating user data as your app evolves.

## Topics

### Essentials
- [Creating a Core Data model](creating-a-core-data-model.md)
  Define your app’s object structure with a data model file.
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)
  Set up the classes that manage and persist your app’s objects.
- [Core Data stack](core-data-stack.md)
  Manage and persist your app’s model layer.
- [Handling Different Data Types in Core Data](handling-different-data-types-in-core-data.md)
  Create, store, and present records for a variety of data types.
- [Linking Data Between Two Core Data Stores](linking-data-between-two-core-data-stores.md)
  Organize data in two different stores and implement a link between them.
### Data modeling
- [Modeling data](modeling-data.md)
  Configure the data model file to contain your app’s object graph.
- [Core Data model](core-data-model.md)
  Describe your app’s object structure.
### Fetch requests
- [class NSFetchRequest](nsfetchrequest.md)
  A description of search criteria used to retrieve data from a persistent store.
- [class NSAsynchronousFetchRequest](nsasynchronousfetchrequest.md)
  A fetch request that retrieves results asynchronously and supports progress notification.
- [class NSAsynchronousFetchResult](nsasynchronousfetchresult.md)
  A fetch result object that encompasses the response from an executed asynchronous fetch request.
- [class NSFetchedResultsController](nsfetchedresultscontroller.md)
  A controller that you use to manage the results of a Core Data fetch request and to display data to the user.
### SwiftData migration and coexistence
- [Adopting SwiftData for a Core Data app](adopting-swiftdata-for-a-core-data-app.md)
  Persist data in your app intuitively with the Swift native persistence framework.
### CloudKit mirroring
- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md)
  Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](synchronizing-a-local-store-to-the-cloud.md)
  Share data between a user’s devices and other iCloud users.
- [class NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md)
  A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.
- [class NSPersistentCloudKitContainerOptions](nspersistentcloudkitcontaineroptions.md)
  An object that customizes how a store description aligns with a CloudKit database.
- [Sharing Core Data objects between iCloud users](sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
### Change processing
- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)
  Guarantee that a context won’t see store changes until you tell it to look.
- [Consuming relevant store changes](consuming-relevant-store-changes.md)
  Filter store transactions for changes relevant to the current view.
- [Persistent history](persistent-history.md)
  Use persistent history tracking to determine what changes have occurred in the store since the enabling of persistent history tracking.
### Background tasks
- [Using Core Data in the background](using-core-data-in-the-background.md)
  Use Core Data in both a single-threaded and multithreaded app.
- [Loading and Displaying a Large Data Feed](../swiftui/loading_and_displaying_a_large_data_feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Conflict resolution](conflict-resolution.md)
  Detect and resolve conflicts that occur when data is changed on multiple threads.
- [Batch processing](batch-processing.md)
  Use batch processes to manage large data changes.
### Data model migration
- [Migrating your data model automatically](migrating-your-data-model-automatically.md)
  Enable lightweight migrations to keep your data model and the underlying data in a consistent state.
- [Staged migrations](staged-migrations.md)
  Migrate complex data models containing changes that are incompatible with lightweight migrations.
- [Manual migrations](manual-migrations.md)
  Migrate elaborate data models with changes that go beyond the capabilities of both lightweight and staged migrations.
### Related types
- [Core Data Constants](core-data-constants.md)
  Keys to use with persistent stores and notifications from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreData)*