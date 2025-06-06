# NSPersistentStoreAsynchronousResult

**Framework**: Core Data  
**Kind**: class

A concrete class used to represent the results of an asynchronous request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSPersistentStoreAsynchronousResult
```

## Topics

### Inspecting the Result
- [var managedObjectContext: NSManagedObjectContext](nspersistentstoreasynchronousresult/managedobjectcontext.md)
  The managed object context for the result.
- [var operationError: (any Error)?](nspersistentstoreasynchronousresult/operationerror.md)
  An error that contains details if the asynchronous fetch request fails.
- [var progress: Progress?](nspersistentstoreasynchronousresult/progress.md)
  An object that reports progress for the asynchronous fetch request.
### Canceling the Result
- [func cancel()](nspersistentstoreasynchronousresult/cancel.md)
  Cancels the asynchronous fetch request.
### Data Types
- [typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock](nspersistentstoreasynchronousfetchresultcompletionblock.md)
  A completion block that an asynchronous fetch request calls with a result.

## Relationships

### Inherits From
- [NSPersistentStoreResult](nspersistentstoreresult.md)
### Inherited By
- [NSAsynchronousFetchResult](nsasynchronousfetchresult.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult)*