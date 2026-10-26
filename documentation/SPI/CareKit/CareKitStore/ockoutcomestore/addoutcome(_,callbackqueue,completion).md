---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/addoutcome(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addOutcome(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addOutcome` asynchronously adds an outcome to the store.

## Declaration

```swift
func addOutcome(_ outcome: Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)
```

## Parameters

- `outcome`: An outcome to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKOutcomeStore Implementations
- [func addOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./addoutcome%28_,callbackqueue,completion%29-4n18v.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/addoutcome(_:callbackqueue:completion:))*