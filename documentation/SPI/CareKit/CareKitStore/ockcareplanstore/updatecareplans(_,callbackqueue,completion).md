---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/updatecareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateCarePlans` asynchronously updates an array of care plans in the store.

## Declaration

```swift
func updateCarePlans(_ plans: [Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)
```

## Parameters

- `plans`: An array of care plans to be updated. The care plans must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/updatecareplans(_:callbackqueue:completion:))*