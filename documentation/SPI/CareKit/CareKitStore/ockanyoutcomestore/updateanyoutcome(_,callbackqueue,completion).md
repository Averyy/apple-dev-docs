---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/updateanyoutcome(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyOutcome(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously update an outcome in the store.

## Declaration

```swift
func updateAnyOutcome(_ outcome: OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)
```

## Parameters

- `outcome`: An outcome that the function updates. The outcome must already exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyOutcomeStore Implementations
- [func updateAnyOutcome(OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)](./updateanyoutcome%28_,callbackqueue,completion%29-8tl0g.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/updateanyoutcome(_:callbackqueue:completion:))*