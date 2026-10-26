---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/addanycareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously adds an array of care plans to the store.

## Declaration

```swift
func addAnyCarePlans(_ plans: [OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)
```

## Parameters

- `plans`: An array of plans to add to the store.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyCarePlanStore Implementations
- [func addAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./addanycareplans%28_,callbackqueue,completion%29-3c5s1.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/addanycareplans(_:callbackqueue:completion:))*