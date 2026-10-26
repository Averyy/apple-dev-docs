---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/addcareplan(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addCarePlan(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addCarePlan` asynchronously adds a care plans to the store.

## Declaration

```swift
func addCarePlan(_ plan: Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)
```

## Parameters

- `plan`: A care plan to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKCarePlanStore Implementations
- [func addCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./addcareplan%28_,callbackqueue,completion%29-5d1lg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/addcareplan(_:callbackqueue:completion:))*