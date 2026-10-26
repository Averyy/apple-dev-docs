---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/updatepatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updatePatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updatePatients` asynchronously updates an array of patients in the store.

## Declaration

```swift
func updatePatients(_ patients: [Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)
```

## Parameters

- `patients`: An array of patients to be updated. The patients must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/updatepatients(_:callbackqueue:completion:))*