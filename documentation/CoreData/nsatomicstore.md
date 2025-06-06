# NSAtomicStore

**Framework**: Core Data  
**Kind**: class

An abstract superclass that you subclass to create a Core Data atomic store.

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
class NSAtomicStore
```

#### Overview

Use an atomic store to handle data sets that can be expressed in memory. The atomic store API favors simplicity over performance.

This class provides default implementations of some utility methods. Create a custom atomic store subclass when you have a custom file format that you want to integrate with a Core Data app. When you create a subclass, override the following [`NSAtomicStore`](nsatomicstore.md) methods:

- [`load()`](nsatomicstore/load().md)
- [`newCacheNode(for:)`](nsatomicstore/newcachenode(for:).md)
- [`newReferenceObject(for:)`](nsatomicstore/newreferenceobject(for:).md)
- [`save()`](nsatomicstore/save().md)
- [`updateCacheNode(_:from:)`](nsatomicstore/updatecachenode(_:from:).md)

Also override the following properties and methods of [`NSPersistentStore`](nspersistentstore.md), from which the atomic store class inherits:

- [`type`](nspersistentstore/type.md)
- [`identifier`](nspersistentstore/identifier.md)
- [`metadata`](nspersistentstore/metadata.md)
- [`metadataForPersistentStore(with:)`](nspersistentstore/metadataforpersistentstore(with:).md)
- [`setMetadata(_:forPersistentStoreAt:)`](nspersistentstore/setmetadata(_:forpersistentstoreat:).md)

`NSAtomicStore` provides a default dictionary of metadata. This dictionary contains the store type and identifier ([`NSStoreTypeKey`](nsstoretypekey.md) and [`NSStoreUUIDKey`](nsstoreuuidkey.md)) as well as store versioning information. Subclasses must ensure that the metadata is saved along with the store data.

## Topics

### Initializing a Store
- [init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, at: URL, options: [AnyHashable : Any]?)](nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:).md)
  Creates an atomic store at the specified location.
### Loading a Store
- [func load() throws](nsatomicstore/load.md)
  Loads the cache nodes for the receiver.
- [func objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](nsatomicstore/objectid(for:withreferenceobject:).md)
  Returns a managed object ID from the reference data for a specified entity.
- [func addCacheNodes(Set<NSAtomicStoreCacheNode>)](nsatomicstore/addcachenodes(_:).md)
  Registers a set of cache nodes with the receiver.
### Updating Cache Nodes
- [func newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode](nsatomicstore/newcachenode(for:).md)
  Returns a new cache node for a given managed object.
- [func newReferenceObject(for: NSManagedObject) -> Any](nsatomicstore/newreferenceobject(for:).md)
  Returns a new reference object for a given managed object.
- [func updateCacheNode(NSAtomicStoreCacheNode, from: NSManagedObject)](nsatomicstore/updatecachenode(_:from:).md)
  Updates the given cache node using the values in a given managed object.
- [func willRemoveCacheNodes(Set<NSAtomicStoreCacheNode>)](nsatomicstore/willremovecachenodes(_:).md)
  Method invoked before the store removes the given collection of cache nodes.
### Saving a Store
- [func save() throws](nsatomicstore/save.md)
  Saves the cache nodes.
### Utility Methods
- [func cacheNodes() -> Set<NSAtomicStoreCacheNode>](nsatomicstore/cachenodes.md)
  Returns the set of cache nodes registered with the receiver.
- [func cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?](nsatomicstore/cachenode(for:).md)
  Returns the cache node for a given managed object ID.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsatomicstore/referenceobject(for:).md)
  Returns the reference object for a given managed object ID.

## Relationships

### Inherits From
- [NSPersistentStore](nspersistentstore.md)
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
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore)*