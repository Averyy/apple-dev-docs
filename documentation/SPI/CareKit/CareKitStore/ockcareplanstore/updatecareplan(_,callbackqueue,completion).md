---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/updatecareplan(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateCarePlan(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateCarePlan` asynchronously updates a care plan in the store.

## Declaration

```swift
func updateCarePlan(_ plan: Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)
```

## Parameters

- `plan`: A care plan to be updated. The care plan must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKCarePlanStore Implementations
- [func updateCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./updatecareplan%28_,callbackqueue,completion%29-7jj26.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/updatecareplan(_:callbackqueue:completion:))*