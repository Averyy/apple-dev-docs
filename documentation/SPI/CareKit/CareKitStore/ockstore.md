---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore"
framework: "CareKit/CareKitStore"
---

# OCKStore

**Framework**: CareKit/CareKitStore  
**Kind**: class  
**Role**: Class

The default store used in CareKit. The underlying database used is CoreData.

## Declaration

```swift
final class OCKStore
```

## Topics

### Operators
- [static func == (OCKStore, OCKStore) -> Bool](./ockstore/eqeq%28_,_%29.md)
  Two instances of `OCKStore` are considered to be equal if they have the same name and store type.
### Initializers
- [init(name: String, securityApplicationGroupIdentifier: String?, type: OCKCoreDataStoreType, remote: OCKRemoteSynchronizable?)](./ockstore/init%28name,securityapplicationgroupidentifier,type,remote%29.md)
  Initialize a new store by specifying its name and store type. Store’s with conflicting names and types must not be created.
### Instance Properties
- [let name: String](./ockstore/name.md)
  The name of the store. When the store type is `onDisk`, this name will be used for the SQLite filename.
- [let securityApplicationGroupIdentifier: String?](./ockstore/securityapplicationgroupidentifier.md)
  App group identifier for a sandboxed app that shares files with other apps from the same developer.
### Instance Methods
- [func delete() throws](./ockstore/delete%28%29.md)
  Completely deletes the store and all its files from disk.
- [func reset() throws](./ockstore/reset%28%29.md)
  Deletes the contents of the store, resetting it to its initial state.
- [func synchronize() async throws](./ockstore/synchronize%28%29.md)
  Synchronizes the on device store with one on a remote server.
- [func synchronize(completion: @Sendable (Error?) -> Void)](./ockstore/synchronize%28completion%29.md)
  Synchronizes the on device store with one on a remote server.
### Default Implementations
- [Equatable Implementations](./ockstore/equatable-implementations.md)
- [OCKAnyCarePlanStore Implementations](./ockstore/ockanycareplanstore-implementations.md)
- [OCKAnyContactStore Implementations](./ockstore/ockanycontactstore-implementations.md)
- [OCKAnyOutcomeStore Implementations](./ockstore/ockanyoutcomestore-implementations.md)
- [OCKAnyPatientStore Implementations](./ockstore/ockanypatientstore-implementations.md)
- [OCKAnyReadOnlyCarePlanStore Implementations](./ockstore/ockanyreadonlycareplanstore-implementations.md)
- [OCKAnyReadOnlyContactStore Implementations](./ockstore/ockanyreadonlycontactstore-implementations.md)
- [OCKAnyReadOnlyEventStore Implementations](./ockstore/ockanyreadonlyeventstore-implementations.md)
- [OCKAnyReadOnlyOutcomeStore Implementations](./ockstore/ockanyreadonlyoutcomestore-implementations.md)
- [OCKAnyReadOnlyPatientStore Implementations](./ockstore/ockanyreadonlypatientstore-implementations.md)
- [OCKAnyReadOnlyTaskStore Implementations](./ockstore/ockanyreadonlytaskstore-implementations.md)
- [OCKAnyTaskStore Implementations](./ockstore/ockanytaskstore-implementations.md)
- [OCKCarePlanStore Implementations](./ockstore/ockcareplanstore-implementations.md)
- [OCKContactStore Implementations](./ockstore/ockcontactstore-implementations.md)
- [OCKOutcomeStore Implementations](./ockstore/ockoutcomestore-implementations.md)
- [OCKPatientStore Implementations](./ockstore/ockpatientstore-implementations.md)
- [OCKReadOnlyEventStore Implementations](./ockstore/ockreadonlyeventstore-implementations.md)
- [OCKReadableCarePlanStore Implementations](./ockstore/ockreadablecareplanstore-implementations.md)
- [OCKReadableContactStore Implementations](./ockstore/ockreadablecontactstore-implementations.md)
- [OCKReadableOutcomeStore Implementations](./ockstore/ockreadableoutcomestore-implementations.md)
- [OCKReadablePatientStore Implementations](./ockstore/ockreadablepatientstore-implementations.md)
- [OCKReadableTaskStore Implementations](./ockstore/ockreadabletaskstore-implementations.md)
- [OCKRemoteSynchronizationDelegate Implementations](./ockstore/ockremotesynchronizationdelegate-implementations.md)
- [OCKTaskStore Implementations](./ockstore/ocktaskstore-implementations.md)

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
- [OCKRemoteSynchronizationDelegate](./ockremotesynchronizationdelegate.md)
- [OCKTaskStore](./ocktaskstore.md)
- Swift.Copyable
- Swift.Equatable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Stores
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
- [protocol OCKAnyResettableStore](./ockanyresettablestore.md)
- [typealias OCKResultClosure](./ockresultclosure.md)
- [struct CareStoreQueryResults](./carestorequeryresults.md)
  A continuous stream of entities that exist in a CareKit store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore)*