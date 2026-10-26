---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/careplanstore(_:shouldhandlequery:)-3scvh"
framework: "CareKit/CareKitStore"
---

# carePlanStore(_:shouldHandleQuery:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.

## Declaration

```swift
func carePlanStore(_ store: OCKAnyReadOnlyCarePlanStore, shouldHandleQuery query: OCKCarePlanQuery) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle the query.
- `query`: The query that is about to be executed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/careplanstore(_:shouldhandlequery:)-3scvh)*