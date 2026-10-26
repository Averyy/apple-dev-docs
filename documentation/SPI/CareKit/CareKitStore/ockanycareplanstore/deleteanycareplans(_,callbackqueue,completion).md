---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/deleteanycareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously deletes an array of care plans from the store.

## Declaration

```swift
func deleteAnyCarePlans(_ plans: [OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)
```

## Parameters

- `plans`: An array of care plans to delete. The care plans must exist in the store.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyCarePlanStore Implementations
- [func deleteAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./deleteanycareplans%28_,callbackqueue,completion%29-6w1h4.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/deleteanycareplans(_:callbackqueue:completion:))*