---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/deleteanytask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously delete a task from the store.

## Declaration

```swift
func deleteAnyTask(_ task: OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)
```

## Parameters

- `task`: A task the function deletes. The task must exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func deleteAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyTask>?)](./deleteanytask%28_,callbackqueue,completion%29-4fgi0.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/deleteanytask(_:callbackqueue:completion:))*