---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcoredatastoretype"
framework: "CareKit/CareKitStore"
---

# OCKCoreDataStoreType

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

An enumerator specifying the type of stores that may be chosen.

## Declaration

```swift
enum OCKCoreDataStoreType
```

## Topics

### Enumeration Cases
- [OCKCoreDataStoreType.inMemory](./ockcoredatastoretype/inmemory.md)
  An in memory store runs in RAM. It is fast and is not persisted between app launches. Its primary use case is for testing.
- [case onDisk(protection: FileProtectionType)](./ockcoredatastoretype/ondisk%28protection%29.md)
  A store that persists data to disk. This option should be used in almost all cases.
### Default Implementations
- [Equatable Implementations](./ockcoredatastoretype/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Stores
- [class OCKStore](./ockstore.md)
  The default store used in CareKit. The underlying database used is CoreData.
- [class OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
  A specialized store that transparently manipulates outcomes in HealthKit.
- [class OCKStoreCoordinator](./ockstorecoordinator.md)
  `OCKStoreCoordinator` is a special kind of pass through store that forwards to a group of other stores. It has different behavior during **read** and **write** operations.
- [enum OCKStoreError](./ockstoreerror.md)
  `OCKStoreError`s will be emitted from `OCKStoreProtocol` conformers if there is problem during a transaction.
- [typealias OCKAnyStoreProtocol](./ockanystoreprotocol.md)
- [typealias OCKStoreProtocol](./ockstoreprotocol.md)
  CareKit can support any store that conforms to this protocol. The `OCKStore` class included in CareKit is a CoreData store that the implements `OCKStoreProtocol` to provide on device storage. Support for other databases such as JSON files, REST API’s, websockets, and 3rd part databases can be added by conforming them to `OCKStoreProtocol`.
- [protocol OCKAnyResettableStore](./ockanyresettablestore.md)
- [typealias OCKResultClosure](./ockresultclosure.md)
- [struct CareStoreQueryResults](./carestorequeryresults.md)
  A continuous stream of entities that exist in a CareKit store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcoredatastoretype)*