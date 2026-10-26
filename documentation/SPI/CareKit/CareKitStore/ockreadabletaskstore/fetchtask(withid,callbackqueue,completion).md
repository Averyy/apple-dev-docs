---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/fetchtask(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchTask(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchTask` asynchronously retrieves an array of tasks from the store using its user-defined unique identifier. If a task with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchTask(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Task>)
```

## Parameters

- `id`: A unique user-defined identifier
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKReadableTaskStore Implementations
- [func fetchTask(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>)](./fetchtask%28withid,callbackqueue,completion%29-28r81.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/fetchtask(withid:callbackqueue:completion:))*