---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/updateanytasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously update an array of tasks in the store.

## Declaration

```swift
func updateAnyTasks(_ tasks: [OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)
```

## Parameters

- `tasks`: An array of tasks that the function updates. The tasks must already exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func updateAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./updateanytasks%28_,callbackqueue,completion%29-2v14s.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/updateanytasks(_:callbackqueue:completion:))*