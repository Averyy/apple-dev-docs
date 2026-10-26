---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/fetchtasks(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchTasks(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchTasks` asynchronously retrieves an array of tasks from the store.

## Declaration

```swift
func fetchTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[Task]>)
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/fetchtasks(query:callbackqueue:completion:))*