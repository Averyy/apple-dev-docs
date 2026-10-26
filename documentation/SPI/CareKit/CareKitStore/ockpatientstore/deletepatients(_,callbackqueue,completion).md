---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deletePatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deletePatients` asynchronously deletes an array of patients from the store.

## Declaration

```swift
func deletePatients(_ patients: [Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)
```

## Parameters

- `patients`: An array of patients to be deleted. The patients must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatients(_:callbackqueue:completion:))*