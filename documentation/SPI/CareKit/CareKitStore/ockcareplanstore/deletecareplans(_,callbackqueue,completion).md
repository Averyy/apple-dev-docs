---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/deletecareplans(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteCarePlans(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteCarePlans` asynchronously deletes an array of care plans from the store.

## Declaration

```swift
func deleteCarePlans(_ plans: [Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)
```

## Parameters

- `plans`: An array of care plans to be deleted. The care plans must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore/deletecareplans(_:callbackqueue:completion:))*