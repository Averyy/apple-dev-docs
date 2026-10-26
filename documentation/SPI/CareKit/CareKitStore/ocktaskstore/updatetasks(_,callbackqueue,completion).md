---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/updatetasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateTasks` asynchronously updates an array of tasks in the store.

## Declaration

```swift
func updateTasks(_ tasks: [Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)
```

## Parameters

- `tasks`: An array of tasks to be updated. The tasks must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/updatetasks(_:callbackqueue:completion:))*