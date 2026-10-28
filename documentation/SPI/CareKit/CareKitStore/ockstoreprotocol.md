---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstoreprotocol"
framework: "CareKit/CareKitStore"
---

# OCKStoreProtocol

**Framework**: CareKit/CareKitStore  
**Kind**: typealias  
**Role**: Type Alias

CareKit can support any store that conforms to this protocol. The `OCKStore` class included in CareKit is a CoreData store that the implements `OCKStoreProtocol` to provide on device storage. Support for other databases such as JSON files, REST API’s, websockets, and 3rd part databases can be added by conforming them to `OCKStoreProtocol`.

## Declaration

```swift
typealias OCKStoreProtocol = OCKPatientStore & OCKCarePlanStore & OCKContactStore & OCKEventStore
```

## Discussion

`OCKStoreProtocol` requires that a minimum level of functionality be provided, and then provides enhanced functionality via protocol extensions. The methods provided by protocol extensions are naive implementations and are not efficient. Developers may wish to use the customization points on `OCKStoreProtocol` to provide more efficient implementations that take advantage of the underlying database’s native features.

> **Remark**: All methods defined in this protocol are required to be implemented as batch operations and should function as transactions. If any one operation should fail, the state of the store should be returned to the state it was in before the transaction began. For example, if an attempt to save an array of 10 outcomes fails on the 6th outcome, the first successfully persisted 6 outcomes must be rolled back to restore the store to the state it was in prior to the transaction.

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
- [enum OCKStoreError](./ockstoreerror.md)
  `OCKStoreError`s will be emitted from `OCKStoreProtocol` conformers if there is problem during a transaction.
- [typealias OCKAnyStoreProtocol](./ockanystoreprotocol.md)
- [protocol OCKAnyResettableStore](./ockanyresettablestore.md)
- [typealias OCKResultClosure](./ockresultclosure.md)
- [struct CareStoreQueryResults](./carestorequeryresults.md)
  A continuous stream of entities that exist in a CareKit store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstoreprotocol)*