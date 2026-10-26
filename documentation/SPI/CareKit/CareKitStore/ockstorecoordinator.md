---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator"
framework: "CareKit/CareKitStore"
---

# OCKStoreCoordinator

**Framework**: CareKit/CareKitStore  
**Kind**: class  
**Role**: Class

`OCKStoreCoordinator` is a special kind of pass through store that forwards to a group of other stores. It has different behavior during **read** and **write** operations.

## Declaration

```swift
final class OCKStoreCoordinator
```

#### Overview

When objects are **fetched** from an `OCKStoreCoordinator`, the `OCKStoreCoordinator` will transparently query all of the stores it knows about and return the aggregated results.

When objects are **added**, **updated**, or **deleted**, a `OCKStoreCoordinator` will attempt to find a single store that can accept responsibility for all the objects that need to be written, and direct the work to that store. If the objects do not all belong to a single store, then the write operation will fail. This is to ensure that write operations are transactional.

> **Note**: The order in which stores are registered on an `OCKStoreCoordinator` is important. If two or more stores are capable of writing an object, the one that was registered first will be given precedence.

## Topics

### Initializers
- [init()](./ockstorecoordinator/init%28%29.md)
### Instance Properties
- [var delegate: OCKStoreCoordinatorDelegate?](./ockstorecoordinator/delegate.md)
### Instance Methods
- [func attach(contactStore: OCKAnyContactStore)](./ockstorecoordinator/attach%28contactstore%29.md)
  Attaches a new store. The new store must be capable of reading and writing contacts.
- [func attach(eventStore: OCKAnyEventStore)](./ockstorecoordinator/attach%28eventstore%29.md)
  Attaches a new store. The new store must be capable of reading and writing tasks and outcomes.
- [func attach(patientStore: OCKAnyPatientStore)](./ockstorecoordinator/attach%28patientstore%29.md)
  Attaches a new store. The new store must be capable of reading and writing patients.
- [func attach(planStore: OCKAnyCarePlanStore)](./ockstorecoordinator/attach%28planstore%29.md)
  Attaches a new store. The new store must be capable of reading and writing care plans.
- [func attach(store: OCKAnyStoreProtocol)](./ockstorecoordinator/attach%28store%29.md)
  Attaches a new store. The new store must be capable of handling reading and writing to all object types.
- [func attachReadOnly(carePlanStore: OCKAnyReadOnlyCarePlanStore)](./ockstorecoordinator/attachreadonly%28careplanstore%29.md)
  Attaches a new store. The new store must be capable of reading care plans.
- [func attachReadOnly(contactStore: OCKAnyReadOnlyContactStore)](./ockstorecoordinator/attachreadonly%28contactstore%29.md)
  Attaches a new store. The new store must be capable of reading contacts.
- [func attachReadOnly(eventStore: OCKAnyReadOnlyEventStore)](./ockstorecoordinator/attachreadonly%28eventstore%29.md)
  Attaches a new store. The new store must be capable of reading events.
- [func attachReadOnly(patientStore: OCKAnyReadOnlyPatientStore)](./ockstorecoordinator/attachreadonly%28patientstore%29.md)
  Attaches a new store. The new store must be capable of reading patients.
- [func reset() throws](./ockstorecoordinator/reset%28%29.md)
### Default Implementations
- [OCKAnyCarePlanStore Implementations](./ockstorecoordinator/ockanycareplanstore-implementations.md)
- [OCKAnyContactStore Implementations](./ockstorecoordinator/ockanycontactstore-implementations.md)
- [OCKAnyOutcomeStore Implementations](./ockstorecoordinator/ockanyoutcomestore-implementations.md)
- [OCKAnyPatientStore Implementations](./ockstorecoordinator/ockanypatientstore-implementations.md)
- [OCKAnyReadOnlyCarePlanStore Implementations](./ockstorecoordinator/ockanyreadonlycareplanstore-implementations.md)
- [OCKAnyReadOnlyContactStore Implementations](./ockstorecoordinator/ockanyreadonlycontactstore-implementations.md)
- [OCKAnyReadOnlyEventStore Implementations](./ockstorecoordinator/ockanyreadonlyeventstore-implementations.md)
- [OCKAnyReadOnlyOutcomeStore Implementations](./ockstorecoordinator/ockanyreadonlyoutcomestore-implementations.md)
- [OCKAnyReadOnlyPatientStore Implementations](./ockstorecoordinator/ockanyreadonlypatientstore-implementations.md)
- [OCKAnyReadOnlyTaskStore Implementations](./ockstorecoordinator/ockanyreadonlytaskstore-implementations.md)
- [OCKAnyTaskStore Implementations](./ockstorecoordinator/ockanytaskstore-implementations.md)
- [OCKStoreCoordinatorDelegate Implementations](./ockstorecoordinator/ockstorecoordinatordelegate-implementations.md)

## Relationships

### Conforms To
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
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- [OCKStoreCoordinatorDelegate](./ockstorecoordinatordelegate.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator)*