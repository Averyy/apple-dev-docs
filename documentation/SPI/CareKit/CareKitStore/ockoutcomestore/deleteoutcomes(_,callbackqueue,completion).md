---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/deleteoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteOutcomes` asynchronously deletes an array of outcomes from the store.

## Declaration

```swift
func deleteOutcomes(_ outcomes: [Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)
```

## Parameters

- `outcomes`: An array of outcomes to be deleted. The outcomes must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/deleteoutcomes(_:callbackqueue:completion:))*