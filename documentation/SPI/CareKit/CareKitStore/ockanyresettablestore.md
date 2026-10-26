---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyresettablestore"
framework: "CareKit/CareKitStore"
---

# OCKAnyResettableStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol OCKAnyResettableStore : AnyObject, Sendable
```

## Topics

### Instance Methods
- [func reset() throws](./ockanyresettablestore/reset%28%29.md)

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyCarePlanStore](./ockanycareplanstore.md)
- [OCKAnyContactStore](./ockanycontactstore.md)
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyPatientStore](./ockanypatientstore.md)
- [OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
- [OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- [OCKCarePlanStore](./ockcareplanstore.md)
- [OCKContactStore](./ockcontactstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
- [OCKPatientStore](./ockpatientstore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
- [OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
- [OCKReadableContactStore](./ockreadablecontactstore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
- [OCKReadablePatientStore](./ockreadablepatientstore.md)
- [OCKReadableTaskStore](./ockreadabletaskstore.md)
- [OCKTaskStore](./ocktaskstore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

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
- [typealias OCKStoreProtocol](./ockstoreprotocol.md)
  CareKit can support any store that conforms to this protocol. The `OCKStore` class included in CareKit is a CoreData store that the implements `OCKStoreProtocol` to provide on device storage. Support for other databases such as JSON files, REST API’s, websockets, and 3rd part databases can be added by conforming them to `OCKStoreProtocol`.
- [typealias OCKResultClosure](./ockresultclosure.md)
- [struct CareStoreQueryResults](./carestorequeryresults.md)
  A continuous stream of entities that exist in a CareKit store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyresettablestore)*