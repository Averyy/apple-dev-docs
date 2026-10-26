---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/deleteanyoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously delete an array of outcomes from the store.

## Declaration

```swift
func deleteAnyOutcomes(_ outcomes: [OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)
```

## Parameters

- `outcomes`: An array of outcomes to be deleted. The outcomes must exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyOutcomeStore Implementations
- [func deleteAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./deleteanyoutcomes%28_,callbackqueue,completion%29-2cje9.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/deleteanyoutcomes(_:callbackqueue:completion:))*