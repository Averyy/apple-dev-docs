# NSAtomicStoreCacheNode

**Framework**: Core Data  
**Kind**: class

A concrete class that you use to represent basic nodes in a Core Data atomic store.

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
class NSAtomicStoreCacheNode
```

#### Overview

A node represents a single record in a persistent store.

You can subclass `NSAtomicStoreCacheNode` to provide custom behavior.

## Topics

### Initializing a Cache Node
- [init(objectID: NSManagedObjectID)](nsatomicstorecachenode/init(objectid:).md)
  Returns a cache node for the given managed object ID.
### Managing Node Data
- [var objectID: NSManagedObjectID](nsatomicstorecachenode/objectid.md)
  The managed object ID of the node.
- [var propertyCache: NSMutableDictionary?](nsatomicstorecachenode/propertycache.md)
  The property cache dictionary of the node.
- [func value(forKey: String) -> Any?](nsatomicstorecachenode/value(forkey:).md)
  Returns the value for a given key.
- [func setValue(Any?, forKey: String)](nsatomicstorecachenode/setvalue(_:forkey:).md)
  Sets the value for the given key.

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
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode)*