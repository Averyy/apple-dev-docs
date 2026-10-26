---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/deleteanytasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously delete an array of tasks from the store.

## Declaration

```swift
func deleteAnyTasks(_ tasks: [OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)
```

## Parameters

- `tasks`: An array of tasks that the function deletes. The tasks must exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func deleteAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./deleteanytasks%28_,callbackqueue,completion%29-9esob.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/deleteanytasks(_:callbackqueue:completion:))*