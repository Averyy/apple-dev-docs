---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/fetchoutcomes(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchOutcomes(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetch a list of events that exist in the store.

## Declaration

```swift
func fetchOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[Outcome]>)
```

#### Discussion

The completion will be called with an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match outcomes in the store. If the query doesn’t contain a date interval, the result will contain the latest version of each outcome. If the query does contain a date interval, the result will contain outcomes whose events occur within the interval.

This method does not check if an outcome’s task is effective in the query interval.

## Parameters

- `query`: Used to match outcomes in the store.
- `callbackQueue`: The queue that runs the completion. In most cases this should be the main queue.
- `completion`: A callback that contains the result.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/fetchoutcomes(query:callbackqueue:completion:))*