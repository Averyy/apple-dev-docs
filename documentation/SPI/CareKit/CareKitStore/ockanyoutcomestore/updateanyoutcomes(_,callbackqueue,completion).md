---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/updateanyoutcomes(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyOutcomes(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously update an array of outcomes in the store.

## Declaration

```swift
func updateAnyOutcomes(_ outcomes: [OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)
```

## Parameters

- `outcomes`: An array of updated outcomes. The outcomes must already exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyOutcomeStore Implementations
- [func updateAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./updateanyoutcomes%28_,callbackqueue,completion%29-77oyg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/updateanyoutcomes(_:callbackqueue:completion:))*