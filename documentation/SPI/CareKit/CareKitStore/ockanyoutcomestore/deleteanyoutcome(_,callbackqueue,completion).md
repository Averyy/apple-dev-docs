---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/deleteanyoutcome(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyOutcome(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously delete an outcome from the store.

## Declaration

```swift
func deleteAnyOutcome(_ outcome: OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)
```

## Parameters

- `outcome`: An outcome that the function deletes. The outcome must exist in the store.
- `callbackQueue`: The queue that the function calls the closure on. In most cases this is the main queue.
- `completion`: A callback that the function calls on the provided callback queue.

## Default Implementations

### OCKAnyOutcomeStore Implementations
- [func deleteAnyOutcome(OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)](./deleteanyoutcome%28_,callbackqueue,completion%29-8wa28.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore/deleteanyoutcome(_:callbackqueue:completion:))*