---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/fetchanyoutcome(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyOutcome(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetch an outcome from the store.

## Declaration

```swift
func fetchAnyOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<OCKAnyOutcome>)
```

## Discussion

If more than one outcome matches the query, only the first returns. If no matching outcomes exist, or there is an error accessing the store, the closure receives an error.

Supply a query that’ll be used to match outcomes in the store. If the query doesn’t contain a date interval, the result contains the latest version of each outcome. If the query does contain a date interval, the result contains outcomes whose events occur within the interval.

This method doesn’t check if an outcome’s task is effective in the query interval.

## Parameters

- `query`: Used to match outcomes in the store.
- `callbackQueue`: The queue that runs the closure. In most cases this should be the main queue.
- `completion`: A callback that contains the result.

## Default Implementations

### OCKAnyReadOnlyOutcomeStore Implementations
- [func fetchAnyOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>)](./fetchanyoutcome%28query,callbackqueue,completion%29-5gk1v.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/fetchanyoutcome(query:callbackqueue:completion:))*