---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/fetchanyoutcomes(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyOutcomes(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetch a list of outcomes that exist in the store.

## Declaration

```swift
func fetchAnyOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[OCKAnyOutcome]>)
```

#### Discussion

The closure receives an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match outcomes in the store. If the query doesn’t contain a date interval, the result contains the latest version of each outcome. If the query does contain a date interval, the result contains outcomes whose events occur within the interval.

This method doesn’t check if an outcome’s task is effective in the query interval.

## Parameters

- `query`: Used to match outcomes in the store.
- `callbackQueue`: The queue that runs the closure. In most cases this should be the main queue.
- `completion`: A callback that contains the result.

## Default Implementations

### OCKAnyReadOnlyOutcomeStore Implementations
- [func fetchAnyOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>)](./fetchanyoutcomes%28query,callbackqueue,completion%29-4910w.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/fetchanyoutcomes(query:callbackqueue:completion:))*