---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/anycareplans(matching:)"
framework: "CareKit/CareKitStore"
---

# anyCarePlans(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of care plans that exist in the store.

## Declaration

```swift
func anyCarePlans(matching query: OCKCarePlanQuery) -> CareStoreQueryResults<OCKAnyCarePlan>
```

#### Discussion

The stream yields a new value whenever the result changes, and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match care plans in the store. If the query doesn’t contain a date interval, the result contains every version of a care plan. Multiple versions of the same care plan have the same [`id`](../ockanycareplan/id.md) but a different UUID. If the query does contain a date interval, the result contains the newest version of a care plan that exists in the interval.

## Parameters

- `query`: Used to match care plans in the store.

## Default Implementations

### OCKAnyReadOnlyCarePlanStore Implementations
- [func anyCarePlans(matching: OCKCarePlanQuery) -> CareStoreQueryResults<OCKAnyCarePlan>](./anycareplans%28matching%29-81hwg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/anycareplans(matching:))*