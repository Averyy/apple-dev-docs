---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/addanyoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously add an array of outcomes to the store.

## Declaration

```swift
func addAnyOutcomes(_ outcomes: [OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)
```

## Parameters

- `outcomes`: An array of outcomes to add to the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyOutcomeStore Implementations
- [func addAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./addanyoutcomes%28_,callbackqueue,completion%29-9bmqe.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/addanyoutcomes(_:callbackqueue:completion:))*