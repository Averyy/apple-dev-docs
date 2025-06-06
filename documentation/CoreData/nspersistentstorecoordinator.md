# NSPersistentStoreCoordinator

**Framework**: Core Data  
**Kind**: class

An object that enables an app’s contexts and the underlying persistent stores to work together.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSPersistentStoreCoordinator
```

## Mentions

- [Setting up a Core Data stack manually](setting-up-a-core-data-stack-manually.md)
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Overview

A managed object context uses a coordinator to facilitate the persistence of its entities in the coordinator’s registered stores. A context can’t function without a coordinator because it relies on the coordinator’s access to the managed object model. The coordinator presents its registered stores as an aggregate, allowing a context to operate on the union of those stores instead of on each individually. A coordinator performs its work on a private queue and executes that work serially. You can use multiple coordinators if the work requires separate queues.

Use a coordinator to add or remove persistent stores, change the type or location on-disk of those stores, query the metadata of a specific store, defer a store’s migrations, determine whether two objects originate from the same store, and so on.

## Topics

### Creating a persistent store coordinator
- [init(managedObjectModel: NSManagedObjectModel)](nspersistentstorecoordinator/init(managedobjectmodel:).md)
  Creates a persistent store coordinator with the specified managed object model.
- [Store options](store-options.md)
  The options keys that configure the behavior and characteristics of a persistent store.
- [Migration options](migration-options.md)
  The options keys that configure the migration behavior of a persistent store.
- [Store versions](store-versions.md)
  The metadata keys you use when comparing store versions.
### Managing configuration
- [var name: String?](nspersistentstorecoordinator/name.md)
  The coordinator’s name.
- [var managedObjectModel: NSManagedObjectModel](nspersistentstorecoordinator/managedobjectmodel.md)
  The coordinator’s managed object model.
- [var persistentStores: [NSPersistentStore]](nspersistentstorecoordinator/persistentstores.md)
  The coordinator’s persistent stores.
### Registering store types
- [class func registerStoreClass(AnyClass?, type: NSPersistentStore.StoreType)](nspersistentstorecoordinator/registerstoreclass(_:type:).md)
  Registers a persistent store subclass using the specified store type.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.
- [class var registeredStoreTypes: [String : NSValue]](nspersistentstorecoordinator/registeredstoretypes.md)
  The coordinator’s registered store types.
### Adding or removing a store
- [func addPersistentStore(type: NSPersistentStore.StoreType, configuration: String?, at: URL, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(type:configuration:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(with: NSPersistentStoreDescription, completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](nspersistentstorecoordinator/addpersistentstore(with:completionhandler:).md)
  Adds a persistent store using the provided description.
- [func remove(NSPersistentStore) throws](nspersistentstorecoordinator/remove(_:).md)
  Removes the specified persistent store from the coordinator.
### Modifying a store
- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:type:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:).md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.
### Managing a store’s location
- [func setURL(URL, for: NSPersistentStore) -> Bool](nspersistentstorecoordinator/seturl(_:for:).md)
  Changes the location of the specified persistent store.
- [func persistentStore(for: URL) -> NSPersistentStore?](nspersistentstorecoordinator/persistentstore(for:).md)
  Returns the persistent store for the specified file URL.
- [func url(for: NSPersistentStore) -> URL](nspersistentstorecoordinator/url(for:).md)
  Returns the location of the provided persistent store.
### Managing a store’s metadata
- [class func setMetadata([String : Any]?, type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:type:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(type: NSPersistentStore.StoreType, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(type:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [func metadata(for: NSPersistentStore) -> [String : Any]](nspersistentstorecoordinator/metadata(for:).md)
  Returns the metadata of the specified persistent store.
- [func setMetadata([String : Any]?, for: NSPersistentStore)](nspersistentstorecoordinator/setmetadata(_:for:).md)
  Updates the metadata for the specified persistent store.
- [let NSStoreTypeKey: String](nsstoretypekey.md)
  A key that identifies the store type.
- [let NSStoreUUIDKey: String](nsstoreuuidkey.md)
  A key that provides the store’s UUID.
### Deferring a store’s migrations
- [let NSPersistentStoreDeferredLightweightMigrationOptionKey: String](nspersistentstoredeferredlightweightmigrationoptionkey.md)
  The key for enabling deferred lightweight migrations.
- [func finishDeferredLightweightMigrationTask() throws](nspersistentstorecoordinator/finishdeferredlightweightmigrationtask.md)
  Executes a single pending task of a deferred lightweight migration.
- [func finishDeferredLightweightMigration() throws](nspersistentstorecoordinator/finishdeferredlightweightmigration.md)
  Executes all remaining tasks of a deferred lightweight migration.
### Performing tasks
- [func perform<T>(() throws -> T) async rethrows -> T](nspersistentstorecoordinator/perform(_:)-74udx.md)
  Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nspersistentstorecoordinator/performandwait(_:)-15ude.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](nspersistentstorecoordinator/execute(_:with:).md)
  Executes the specified request on each of the coordinator’s persistent stores.
### Maintaining a record of changes
- [let NSPersistentHistoryTrackingKey: String](nspersistenthistorytrackingkey.md)
  The key you use to enable persistent history tracking.
- [func currentPersistentHistoryToken(fromStores: [Any]?) -> NSPersistentHistoryToken?](nspersistentstorecoordinator/currentpersistenthistorytoken(fromstores:).md)
  Returns a single persistent history token representing all of the specified stores.
### Integrating with Spotlight
- [let NSCoreDataCoreSpotlightExporter: String](nscoredatacorespotlightexporter.md)
  The key you use to specify your Core Spotlight delegate.
- [class NSCoreDataCoreSpotlightDelegate](nscoredatacorespotlightdelegate.md)
  A set of methods that enable integration with Core Spotlight.
- [Spotlight record keys](spotlight-record-keys.md)
  The keys for the values that exist in Spotlight’s external record files.
- [Showcase App Data in Spotlight](showcase-app-data-in-spotlight.md)
  Index app data so users can find it by using Spotlight search.
### Getting individual object identifiers
- [func managedObjectID(forURIRepresentation: URL) -> NSManagedObjectID?](nspersistentstorecoordinator/managedobjectid(forurirepresentation:).md)
  Returns the object identifier for the specified URI representation.
### Responding to changes of the coordinator’s registered stores
- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](../foundation/nsnotification/name/1468800-nspersistentstorecoordinatorstor.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](../foundation/nsnotification/name/1468925-nspersistentstorecoordinatorstor.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](../foundation/nsnotification/name/1468876-nspersistentstorecoordinatorwill.md)
  A notification that posts before a coordinator removes a store.
- [Notification keys](notification-keys.md)
  The keys you use to retrieve values from a notification’s user info dictionary.
### Deprecated
- [Deprecated Symbols](nspersistentstorecoordinator-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Methods
- [func managedObjectID(for: String) -> NSManagedObjectID?](nspersistentstorecoordinator/managedobjectid(for:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSLocking](../Foundation/NSLocking.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSPersistentStore](nspersistentstore.md)
  The abstract base class for all Core Data persistent stores.
- [class NSPersistentStoreDescription](nspersistentstoredescription.md)
  A description object used to create and load a persistent store.
- [class NSPersistentStoreRequest](nspersistentstorerequest.md)
  Criteria used to retrieve data from or save data to a persistent store.
- [class NSPersistentStoreResult](nspersistentstoreresult.md)
  The abstract base class for results returned from a persistent store coordinator.
- [class NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)
  A concrete class used to represent the results of an asynchronous request.
- [class NSSaveChangesRequest](nssavechangesrequest.md)
  An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [class NSAtomicStore](nsatomicstore.md)
  An abstract superclass that you subclass to create a Core Data atomic store.
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator)*