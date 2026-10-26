---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/fetchanycareplan(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyCarePlan(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously retrieves a single care plan from the store.

## Declaration

```swift
func fetchAnyCarePlan(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<OCKAnyCarePlan>)
```

## Parameters

- `id`: The identifier of the fetched item.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyCarePlanStore Implementations
- [func fetchAnyCarePlan(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>)](./fetchanycareplan%28withid,callbackqueue,completion%29-8sq9c.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore/fetchanycareplan(withid:callbackqueue:completion:))*