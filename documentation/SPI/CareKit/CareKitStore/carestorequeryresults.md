---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults"
framework: "CareKit/CareKitStore"
---

# CareStoreQueryResults

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A continuous stream of entities that exist in a CareKit store.

## Declaration

```swift
struct CareStoreQueryResults<Result>
```

## Overview

You can’t instantiate this stream directly. Instead, use methods like [`tasks(matching:)`](./ockreadabletaskstore/tasks%28matching%29.md) to create one. Similarly named methods exist for streaming other entities in a store.

## Topics

### Structures
- [CareStoreQueryResults.AsyncIterator](./carestorequeryresults/asynciterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncIterator](./carestorequeryresults/makeasynciterator%28%29.md)
### Default Implementations
- [AsyncSequence Implementations](./carestorequeryresults/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence

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
- [protocol OCKAnyResettableStore](./ockanyresettablestore.md)
- [typealias OCKResultClosure](./ockresultclosure.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/carestorequeryresults)*