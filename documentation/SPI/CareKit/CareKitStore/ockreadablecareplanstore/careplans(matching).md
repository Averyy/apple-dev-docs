---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/careplans(matching:)"
framework: "CareKit/CareKitStore"
---

# carePlans(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of care plans that exist in the store.

## Declaration

```swift
func carePlans(matching query: OCKCarePlanQuery) -> Plans
```

## Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match care plans in the store. If the query doesn’t contain a date interval, the result will contain every version of a care plan. Multiple versions of the same care plan will have the same [`id`](../ockanycareplan/id.md) but a different UUID. If the query does contain a date interval, the result will contain the newest version of a care plan that exists in the interval.

## Parameters

- `query`: Used to match care plans in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/careplans(matching:))*