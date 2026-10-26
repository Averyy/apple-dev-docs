---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore/fetchanyevent(fortask:occurrence:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyEvent(forTask:occurrence:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchAnyEvent` retrieves the occurrence of the specified task.

## Declaration

```swift
func fetchAnyEvent(forTask task: OCKAnyTask, occurrence: Int, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<OCKAnyEvent>)
```

## Parameters

- `task`: The task for which to retrieve an event.
- `occurrence`: The occurrence number of the event to be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyEventStore Implementations
- [func fetchAnyEvent(forTask: OCKAnyTask, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyEvent>)](./fetchanyevent%28fortask,occurrence,callbackqueue,completion%29-2dpwq.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore/fetchanyevent(fortask:occurrence:callbackqueue:completion:))*