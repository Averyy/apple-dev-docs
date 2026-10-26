---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/deletecareplan(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteCarePlan(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteCarePlan` asynchronously deletes a care plan from the store.

## Declaration

```swift
func deleteCarePlan(_ plan: Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)
```

## Parameters

- `plan`: A care plan to be deleted. The care plan must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKCarePlanStore Implementations
- [func deleteCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./deletecareplan%28_,callbackqueue,completion%29-2c0r8.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/deletecareplan(_:callbackqueue:completion:))*