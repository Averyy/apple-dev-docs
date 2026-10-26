---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytasks(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyTasks(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously retrieve an array of tasks from the store.

## Declaration

```swift
func fetchAnyTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[OCKAnyTask]>)
```

## Parameters

- `query`: A query that constrain the fetched values.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyTaskStore Implementations
- [func fetchAnyTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>)](./fetchanytasks%28query,callbackqueue,completion%29-7cjv9.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytasks(query:callbackqueue:completion:))*