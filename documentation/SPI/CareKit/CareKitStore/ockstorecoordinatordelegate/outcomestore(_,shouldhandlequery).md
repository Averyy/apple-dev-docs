---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/outcomestore(_:shouldhandlequery:)"
framework: "CareKit/CareKitStore"
---

# outcomeStore(_:shouldHandleQuery:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.

## Declaration

```swift
func outcomeStore(_ store: OCKAnyReadOnlyOutcomeStore, shouldHandleQuery query: OCKOutcomeQuery) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle the query.
- `query`: The query that is about to be executed.

## Default Implementations

### OCKStoreCoordinatorDelegate Implementations
- [func outcomeStore(OCKAnyReadOnlyOutcomeStore, shouldHandleQuery: OCKOutcomeQuery) -> Bool](./outcomestore%28_,shouldhandlequery%29-21piq.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/outcomestore(_:shouldhandlequery:))*