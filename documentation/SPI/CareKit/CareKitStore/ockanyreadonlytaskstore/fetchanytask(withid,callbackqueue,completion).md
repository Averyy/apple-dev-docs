---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytask(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyTask(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously retrieve an array of tasks from the store using its user-defined unique identifier.

## Declaration

```swift
func fetchAnyTask(withID id: String, callbackQueue: DispatchQueue, completion: @escaping @Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)
```

## Discussion

If a task with the specified identifier isn’t found, the completion handler receives an error.

## Parameters

- `id`: The identifier of the item to fetch.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyTaskStore Implementations
- [func fetchAnyTask(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyTask>)](./fetchanytask%28withid,callbackqueue,completion%29-29hbm.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlytaskstore/fetchanytask(withid:callbackqueue:completion:))*