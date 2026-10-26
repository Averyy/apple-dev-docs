---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/updateoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateOutcomes` asynchronously updates an array of outcomes in the store.

## Declaration

```swift
func updateOutcomes(_ outcomes: [Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)
```

## Parameters

- `outcomes`: An array of outcomes to be updated. The outcomes must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/updateoutcomes(_:callbackqueue:completion:))*