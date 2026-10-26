---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/updateanycareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously updates an array of care plans in the store.

## Declaration

```swift
func updateAnyCarePlans(_ plans: [OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)
```

## Parameters

- `plans`: An array of care plans to update in the store. The care plans must already exist in the store.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyCarePlanStore Implementations
- [func updateAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./updateanycareplans%28_,callbackqueue,completion%29-2067m.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/updateanycareplans(_:callbackqueue:completion:))*