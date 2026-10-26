---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/deleteoutcome(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteOutcome(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteOutcome` asynchronously deletes an outcome from the store.

## Declaration

```swift
func deleteOutcome(_ outcome: Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)
```

## Parameters

- `outcome`: An outcome to be deleted. The outcome must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKOutcomeStore Implementations
- [func deleteOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./deleteoutcome%28_,callbackqueue,completion%29-8mwzt.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore/deleteoutcome(_:callbackqueue:completion:))*