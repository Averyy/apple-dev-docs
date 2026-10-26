---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/updatetask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateTask` asynchronously updates a task in the store.

## Declaration

```swift
func updateTask(_ task: Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)
```

## Parameters

- `task`: A task to be updated. The task must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKTaskStore Implementations
- [func updateTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./updatetask%28_,callbackqueue,completion%29-2npu1.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/updatetask(_:callbackqueue:completion:))*