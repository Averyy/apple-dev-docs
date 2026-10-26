---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/fetchanycareplans(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyCarePlans(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of care plans that exist in the store. The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

## Declaration

```swift
func fetchAnyCarePlans(query: OCKCarePlanQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[OCKAnyCarePlan]>)
```

#### Discussion

Supply a query that’ll be used to match care plans in the store. If the query doesn’t contain a date interval, the result contains every version of a care plan. Multiple versions of the same care plan have the same [`id`](../ockanycareplan/id.md) but a different UUID. If the query does contain a date interval, the result contains the newest version of a care plan that exists in the interval.

## Parameters

- `query`: A query that constrains care plans the method fetches.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyCarePlanStore Implementations
- [func fetchAnyCarePlans(query: OCKCarePlanQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>)](./fetchanycareplans%28query,callbackqueue,completion%29-3x1lm.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/fetchanycareplans(query:callbackqueue:completion:))*