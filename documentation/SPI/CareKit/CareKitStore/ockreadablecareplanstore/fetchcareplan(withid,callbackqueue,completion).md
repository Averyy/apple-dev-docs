---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/fetchcareplan(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchCarePlan(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchCarePlan` asynchronously retrieves a care plan from the store using its user-defined unique identifier. If a care plan with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchCarePlan(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Plan>)
```

## Parameters

- `id`: A unique user-defined identifier
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKReadableCarePlanStore Implementations
- [func fetchCarePlan(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>)](./fetchcareplan%28withid,callbackqueue,completion%29-9syxq.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/fetchcareplan(withid:callbackqueue:completion:))*