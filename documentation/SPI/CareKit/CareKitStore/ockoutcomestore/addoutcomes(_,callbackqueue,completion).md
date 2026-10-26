---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/addoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addOutcomes` asynchronously adds an array of outcomes to the store.

## Declaration

```swift
func addOutcomes(_ outcomes: [Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)
```

## Parameters

- `outcomes`: An array of outcomes to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/addoutcomes(_:callbackqueue:completion:))*