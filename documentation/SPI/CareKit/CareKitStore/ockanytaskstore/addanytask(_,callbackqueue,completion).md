---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/addanytask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously add a task to the store.

## Declaration

```swift
func addAnyTask(_ task: OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)
```

## Parameters

- `task`: A task the function adds to the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func addAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyTask>?)](./addanytask%28_,callbackqueue,completion%29-34yei.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/addanytask(_:callbackqueue:completion:))*