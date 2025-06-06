# NSPersistentStoreRequest

**Framework**: Core Data  
**Kind**: class

Criteria used to retrieve data from or save data to a persistent store.

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
class NSPersistentStoreRequest
```

## Topics

### Configuring a Request
- [var affectedStores: [NSPersistentStore]?](nspersistentstorerequest/affectedstores.md)
  The stores the request should be sent to.
- [var requestType: NSPersistentStoreRequestType](nspersistentstorerequest/requesttype.md)
  The type of the fetch request.
- [enum NSPersistentStoreRequestType](nspersistentstorerequesttype.md)
  Constants that specify the types of fetch requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSAsynchronousFetchRequest](nsasynchronousfetchrequest.md)
- [NSBatchDeleteRequest](nsbatchdeleterequest.md)
- [NSBatchInsertRequest](nsbatchinsertrequest.md)
- [NSBatchUpdateRequest](nsbatchupdaterequest.md)
- [NSFetchRequest](nsfetchrequest.md)
- [NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
- [NSPersistentHistoryChangeRequest](nspersistenthistorychangerequest.md)
- [NSSaveChangesRequest](nssavechangesrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)
  An object that enables an app’s contexts and the underlying persistent stores to work together.
- [class NSPersistentStore](nspersistentstore.md)
  The abstract base class for all Core Data persistent stores.
- [class NSPersistentStoreDescription](nspersistentstoredescription.md)
  A description object used to create and load a persistent store.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)*