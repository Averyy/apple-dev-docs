---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/addtasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addTasks` asynchronously adds an array of tasks to the store.

## Declaration

```swift
func addTasks(_ tasks: [Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)
```

## Parameters

- `tasks`: An array of tasks to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/addtasks(_:callbackqueue:completion:))*