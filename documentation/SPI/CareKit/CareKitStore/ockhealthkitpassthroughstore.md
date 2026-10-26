---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore"
framework: "CareKit/CareKitStore"
---

# OCKHealthKitPassthroughStore

**Framework**: CareKit/CareKitStore  
**Kind**: class  
**Role**: Class

A specialized store that transparently manipulates outcomes in HealthKit.

## Declaration

```swift
final class OCKHealthKitPassthroughStore
```

## Topics

### Initializers
- [init(store: OCKStore)](./ockhealthkitpassthroughstore/init%28store%29.md)
### Instance Methods
- [func checkAbilityToDelete(outcomes: [OCKHealthKitOutcome]) throws](./ockhealthkitpassthroughstore/checkabilitytodelete%28outcomes%29.md)
- [func fetchTasks(for: [OCKHealthKitOutcome]) throws -> [OCKHealthKitTask]](./ockhealthkitpassthroughstore/fetchtasks%28for%29.md)
- [func requestHealthKitPermissionsForAllTasksInStore(completion: @Sendable (Error?) -> Void)](./ockhealthkitpassthroughstore/requesthealthkitpermissionsforalltasksinstore%28completion%29.md)
  Presents a standard HealthKit permission sheet prompting the user to grant permission for all data types required to read and write outcomes for the tasks in this store.
- [func reset() throws](./ockhealthkitpassthroughstore/reset%28%29.md)
  Deletes the contents of the store, resetting it to its initial state.
### Type Aliases
- [OCKHealthKitPassthroughStore.Outcome](./ockhealthkitpassthroughstore/outcome.md)
- [OCKHealthKitPassthroughStore.Task](./ockhealthkitpassthroughstore/task.md)
### Default Implementations
- [OCKAnyOutcomeStore Implementations](./ockhealthkitpassthroughstore/ockanyoutcomestore-implementations.md)
- [OCKAnyReadOnlyEventStore Implementations](./ockhealthkitpassthroughstore/ockanyreadonlyeventstore-implementations.md)
- [OCKAnyReadOnlyOutcomeStore Implementations](./ockhealthkitpassthroughstore/ockanyreadonlyoutcomestore-implementations.md)
- [OCKAnyReadOnlyTaskStore Implementations](./ockhealthkitpassthroughstore/ockanyreadonlytaskstore-implementations.md)
- [OCKAnyTaskStore Implementations](./ockhealthkitpassthroughstore/ockanytaskstore-implementations.md)
- [OCKOutcomeStore Implementations](./ockhealthkitpassthroughstore/ockoutcomestore-implementations.md)
- [OCKReadOnlyEventStore Implementations](./ockhealthkitpassthroughstore/ockreadonlyeventstore-implementations.md)
- [OCKReadableOutcomeStore Implementations](./ockhealthkitpassthroughstore/ockreadableoutcomestore-implementations.md)
- [OCKReadableTaskStore Implementations](./ockhealthkitpassthroughstore/ockreadabletaskstore-implementations.md)
- [OCKTaskStore Implementations](./ockhealthkitpassthroughstore/ocktaskstore-implementations.md)

## Relationships

### Conforms To
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
- [OCKReadableTaskStore](./ockreadabletaskstore.md)
- [OCKTaskStore](./ocktaskstore.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Stores
- [class OCKStore](./ockstore.md)
  The default store used in CareKit. The underlying database used is CoreData.
- [enum OCKCoreDataStoreType](./ockcoredatastoretype.md)
  An enumerator specifying the type of stores that may be chosen.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore)*