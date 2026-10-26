---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/updateanytask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously update a task in the store.

## Declaration

```swift
func updateAnyTask(_ task: OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)
```

## Parameters

- `task`: A task the function updates. The task must already exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func updateAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyTask>?)](./updateanytask%28_,callbackqueue,completion%29-l725.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/updateanytask(_:callbackqueue:completion:))*