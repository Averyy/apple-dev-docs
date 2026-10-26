---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/addtask(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addTask(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addTask` asynchronously adds a task to the store.

## Declaration

```swift
func addTask(_ task: Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)
```

## Parameters

- `task`: A task to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKTaskStore Implementations
- [func addTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./addtask%28_,callbackqueue,completion%29-4asul.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/addtask(_:callbackqueue:completion:))*