---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstoreerror"
framework: "CareKit/CareKitStore"
---

# OCKStoreError

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

`OCKStoreError`s will be emitted from `OCKStoreProtocol` conformers if there is problem during a transaction.

## Declaration

```swift
enum OCKStoreError
```

## Topics

### Enumeration Cases
- [OCKStoreError.addFailed(reason:)](./ockstoreerror/addfailed%28reason%29.md)
  Occurs when adding an entity fails.
- [OCKStoreError.deleteFailed(reason:)](./ockstoreerror/deletefailed%28reason%29.md)
  Occurs when deleting an existing entity fails.
- [OCKStoreError.fetchFailed(reason:)](./ockstoreerror/fetchfailed%28reason%29.md)
  Occurs when a fetch fails.
- [OCKStoreError.invalidValue(reason:)](./ockstoreerror/invalidvalue%28reason%29.md)
  Occurs when an invalid value is provided.
- [OCKStoreError.remoteSynchronizationFailed(reason:)](./ockstoreerror/remotesynchronizationfailed%28reason%29.md)
  Occurs when synchronization with a remote server fails.
- [OCKStoreError.timedOut(reason:)](./ockstoreerror/timedout%28reason%29.md)
  Occurs when an asynchronous action takes too long.
- [OCKStoreError.updateFailed(reason:)](./ockstoreerror/updatefailed%28reason%29.md)
  Occurs when an update to an existing entity fails.
### Instance Properties
- [var errorDescription: String?](./ockstoreerror/errordescription.md)
### Default Implementations
- [Equatable Implementations](./ockstoreerror/equatable-implementations.md)
- [Error Implementations](./ockstoreerror/error-implementations.md)
- [LocalizedError Implementations](./ockstoreerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Equatable
- Swift.Error
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Stores
- [class OCKStore](./ockstore.md)
  The default store used in CareKit. The underlying database used is CoreData.
- [enum OCKCoreDataStoreType](./ockcoredatastoretype.md)
  An enumerator specifying the type of stores that may be chosen.
- [class OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
  A specialized store that transparently manipulates outcomes in HealthKit.
- [class OCKStoreCoordinator](./ockstorecoordinator.md)
  `OCKStoreCoordinator` is a special kind of pass through store that forwards to a group of other stores. It has different behavior during **read** and **write** operations.
- [typealias OCKAnyStoreProtocol](./ockanystoreprotocol.md)
- [typealias OCKStoreProtocol](./ockstoreprotocol.md)
  CareKit can support any store that conforms to this protocol. The `OCKStore` class included in CareKit is a CoreData store that the implements `OCKStoreProtocol` to provide on device storage. Support for other databases such as JSON files, REST API’s, websockets, and 3rd part databases can be added by conforming them to `OCKStoreProtocol`.
- [protocol OCKAnyResettableStore](./ockanyresettablestore.md)
- [typealias OCKResultClosure](./ockresultclosure.md)
- [struct CareStoreQueryResults](./carestorequeryresults.md)
  A continuous stream of entities that exist in a CareKit store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstoreerror)*