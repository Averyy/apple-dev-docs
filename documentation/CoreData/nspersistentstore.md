# NSPersistentStore

**Framework**: Core Data  
**Kind**: class

The abstract base class for all Core Data persistent stores.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSPersistentStore
```

#### Overview

Core Data provides four store types—SQLite, Binary, XML, and In-Memory (the XML store is not available on iOS); these are described in Persistent Store Features. Core Data also provides subclasses of `NSPersistentStore` that you can use to define your own store types: [`NSAtomicStore`](nsatomicstore.md) and [`NSIncrementalStore`](nsincrementalstore.md). The Binary and XML stores are examples of atomic stores that inherit functionality from `NSAtomicStore`.

##### Subclassing Notes

You should not subclass `NSPersistentStore` directly. Core Data only supports subclassing of [`NSAtomicStore`](nsatomicstore.md) and [`NSIncrementalStore`](nsincrementalstore.md).

The designated initializer is [`init(persistentStoreCoordinator:configurationName:at:options:)`](nspersistentstore/init(persistentstorecoordinator:configurationname:at:options:).md). When you implement the initializer, you must ensure you load metadata during initialization and set it using [`metadata`](nspersistentstore/metadata.md).

You must override these methods:

- [`type`](nspersistentstore/type.md)
- [`metadata`](nspersistentstore/metadata.md)
- [`metadataForPersistentStore(with:)`](nspersistentstore/metadataforpersistentstore(with:).md)
- [`setMetadata(_:forPersistentStoreAt:)`](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)

## Topics

### Creating a Persistent Store
- [init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, at: URL, options: [AnyHashable : Any]?)](nspersistentstore/init(persistentstorecoordinator:configurationname:at:options:).md)
  Returns a store initialized with the given arguments.
### Getting Store Configuration
- [var configurationName: String](nspersistentstore/configurationname.md)
  The name of the managed object model configuration that creates the persistent store.
- [var options: [AnyHashable : Any]?](nspersistentstore/options.md)
  The options that Core Data uses to create the store.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](nspersistentstore/persistentstorecoordinator.md)
  The persistent store coordinator that loads the persistent store.
- [var type: String](nspersistentstore/type.md)
  The type string of the persistent store.
- [NSPersistentStore.StoreType](nspersistentstore/storetype.md)
  The types of persistent stores that Core Data supports.
- [Persistent Store Types](persistent-store-types.md)
  Persist data through the available store types.
### Managing Store Attributes
- [var identifier: String!](nspersistentstore/identifier.md)
  The unique identifier for the persistent store.
- [var isReadOnly: Bool](nspersistentstore/isreadonly.md)
  A Boolean value that indicates whether the persistent store is read-only.
- [var url: URL?](nspersistentstore/url.md)
  The URL for the persistent store.
### Managing Store Metadata
- [class func metadataForPersistentStore(with: URL) throws -> [String : Any]](nspersistentstore/metadataforpersistentstore(with:).md)
  Returns the metadata from the persistent store at the given URL.
- [class func setMetadata([String : Any]?, forPersistentStoreAt: URL) throws](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)
  Sets the metadata for the store at a given URL.
- [func loadMetadata() throws](nspersistentstore/loadmetadata.md)
  Instructs the persistent store to load its metadata.
- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.
### Responding to the Store Life Cycle
- [func didAdd(to: NSPersistentStoreCoordinator)](nspersistentstore/didadd(to:).md)
  Invoked after the persistent store has been added to the persistent store coordinator.
- [func willRemove(from: NSPersistentStoreCoordinator?)](nspersistentstore/willremove(from:).md)
  Invoked before the persistent store is removed from the persistent store coordinator.
### Integrating with Spotlight
- [var coreSpotlightExporter: NSCoreDataCoreSpotlightDelegate](nspersistentstore/corespotlightexporter.md)
  The spotlight exporter associated with this persistent store.
### Providing a Migration Manager
- [class func migrationManagerClass() -> AnyClass](nspersistentstore/migrationmanagerclass.md)
  Returns the migration manager class for this store class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSAtomicStore](nsatomicstore.md)
- [NSIncrementalStore](nsincrementalstore.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)
  An object that enables an app’s contexts and the underlying persistent stores to work together.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore)*