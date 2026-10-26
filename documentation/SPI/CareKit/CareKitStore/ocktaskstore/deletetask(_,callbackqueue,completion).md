---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/deletetask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteTask` asynchronously deletes a task from the store.

## Declaration

```swift
func deleteTask(_ task: Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)
```

## Parameters

- `task`: A task to be deleted. The task must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKTaskStore Implementations
- [func deleteTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./deletetask%28_,callbackqueue,completion%29-8upjg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/deletetask(_:callbackqueue:completion:))*