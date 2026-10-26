---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/addcareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addCarePlans` asynchronously adds an array of care plans to the store.

## Declaration

```swift
func addCarePlans(_ plans: [Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)
```

## Parameters

- `plans`: An array of plans to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/addcareplans(_:callbackqueue:completion:))*