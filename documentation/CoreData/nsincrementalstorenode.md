# NSIncrementalStoreNode

**Framework**: Core Data  
**Kind**: class

A concrete class used to represent basic nodes in a Core Data incremental store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSIncrementalStoreNode
```

#### Overview

A node represents a single record in a persistent store.

You can subclass `NSIncrementalStoreNode` to provide custom behavior.

## Topics

### Initializing a Node
- [init(objectID: NSManagedObjectID, withValues: [String : Any], version: UInt64)](nsincrementalstorenode/init(objectid:withvalues:version:).md)
  Returns an object initialized with the given values.
### Managing Node Data
- [var objectID: NSManagedObjectID](nsincrementalstorenode/objectid.md)
  The object ID that identifies the data stored by the receiver.
- [func update(withValues: [String : Any], version: UInt64)](nsincrementalstorenode/update(withvalues:version:).md)
  Update the values and version to reflect new data being saved to or loaded from the external store.
- [func value(for: NSPropertyDescription) -> Any?](nsincrementalstorenode/value(for:).md)
  Returns the value for the given property.
- [var version: UInt64](nsincrementalstorenode/version.md)
  The version of data in the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class NSAtomicStore](nsatomicstore.md)
  An abstract superclass that you subclass to create a Core Data atomic store.
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)*