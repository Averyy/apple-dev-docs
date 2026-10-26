---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/addanytasks(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyTasks(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously add an array of tasks to the store.

## Declaration

```swift
func addAnyTasks(_ tasks: [OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)
```

## Parameters

- `tasks`: An array of tasks that the function adds.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyTaskStore Implementations
- [func addAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./addanytasks%28_,callbackqueue,completion%29-1esbv.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore/addanytasks(_:callbackqueue:completion:))*