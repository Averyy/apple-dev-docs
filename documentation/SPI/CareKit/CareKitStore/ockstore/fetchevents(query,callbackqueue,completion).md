---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchevents(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchEvents(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Inherited from `OCKReadOnlyEventStore.fetchEvents(query:callbackQueue:completion:)`.

## Declaration

```swift
func fetchEvents(query: OCKEventQuery, callbackQueue: DispatchQueue = .main, completion: @escaping OCKResultClosure<[OCKEvent<Task, Outcome>]>)
```

Available when `Task` conforms to `OCKAnyVersionableTask`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchevents(query:callbackqueue:completion:))*