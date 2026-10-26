---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/updateoutcome(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateOutcome(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateOutcome` asynchronously updates an outcome in the store.

## Declaration

```swift
func updateOutcome(_ outcome: Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)
```

## Parameters

- `outcome`: An outcome to be updated. The outcome must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKOutcomeStore Implementations
- [func updateOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./updateoutcome%28_,callbackqueue,completion%29-zsjk.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/updateoutcome(_:callbackqueue:completion:))*