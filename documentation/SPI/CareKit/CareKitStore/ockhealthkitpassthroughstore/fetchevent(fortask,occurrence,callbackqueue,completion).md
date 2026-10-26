---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchevent(fortask:occurrence:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchEvent(forTask:occurrence:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `OCKReadOnlyEventStore.fetchEvent(forTask:occurrence:callbackQueue:completion:)`.

## Declaration

```swift
func fetchEvent(forTask task: Self.Task, occurrence: Int, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Event>)
```

Available when `Task` conforms to `OCKAnyVersionableTask`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchevent(fortask:occurrence:callbackqueue:completion:))*