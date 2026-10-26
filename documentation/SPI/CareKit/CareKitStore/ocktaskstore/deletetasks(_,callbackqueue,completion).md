---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/deletetasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteTasks` asynchronously deletes an array of tasks from the store.

## Declaration

```swift
func deleteTasks(_ tasks: [Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)
```

## Parameters

- `tasks`: An array of tasks to be deleted. The tasks must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore/deletetasks(_:callbackqueue:completion:))*