---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore/fetchevent(fortask:occurrence:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchEvent(forTask:occurrence:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchEvent` retrieves a single occurrence of the specified task.

## Declaration

```swift
func fetchEvent(forTask task: Task, occurrence: Int, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Event>)
```

## Parameters

- `task`: The task for which to retrieve an event.
- `occurrence`: The occurrence index of the desired event.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the specified queue.

## Default Implementations

### OCKReadOnlyEventStore Implementations
- [func fetchEvent(forTask: Self.Task, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<Event>)](./fetchevent%28fortask,occurrence,callbackqueue,completion%29-298oz.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore/fetchevent(fortask:occurrence:callbackqueue:completion:))*