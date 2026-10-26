---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/addpatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addPatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addPatients` asynchronously adds an array of patients to the store.

## Declaration

```swift
func addPatients(_ patients: [Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)
```

## Parameters

- `patients`: An array of patients to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/addpatients(_:callbackqueue:completion:))*