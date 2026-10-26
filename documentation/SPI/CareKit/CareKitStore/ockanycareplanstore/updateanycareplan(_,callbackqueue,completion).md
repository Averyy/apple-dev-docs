---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/updateanycareplan(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyCarePlan(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously updates a single care plan in the store.

## Declaration

```swift
func updateAnyCarePlan(_ plan: OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)
```

## Parameters

- `plan`: A single care plan to update. The care plans must already exist in the store.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyCarePlanStore Implementations
- [func updateAnyCarePlan(OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)](./updateanycareplan%28_,callbackqueue,completion%29-5ie1n.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/updateanycareplan(_:callbackqueue:completion:))*