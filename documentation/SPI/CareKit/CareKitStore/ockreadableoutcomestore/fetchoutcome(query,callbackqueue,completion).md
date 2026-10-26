---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/fetchoutcome(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchOutcome(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetch a list of events that exist in the store.

## Declaration

```swift
func fetchOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Outcome>)
```

#### Discussion

If more than one outcome matches the query, only the first will be returned. If no matching outcomes exist or there is an error accessing the store, the completion will be called with an error.

Supply a query that’ll be used to match outcomes in the store. If the query doesn’t contain a date interval, the result will contain the latest version of each outcome. If the query does contain a date interval, the result will contain outcomes whose events occur within the interval.

This method does not check if an outcome’s task is effective in the query interval.

## Parameters

- `query`: Used to match outcomes in the store.
- `callbackQueue`: The queue that runs the completion. In most cases this should be the main queue.
- `completion`: A callback that contains the result.

## Default Implementations

### OCKReadableOutcomeStore Implementations
- [func fetchOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>)](./fetchoutcome%28query,callbackqueue,completion%29-2xfgi.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/fetchoutcome(query:callbackqueue:completion:))*