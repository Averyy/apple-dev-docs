---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/updateanypatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyPatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateAnyPatients` asynchronously updates an array of patients in the store.

## Declaration

```swift
func updateAnyPatients(_ patients: [OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)
```

## Parameters

- `patients`: An array of patients to be updated. The patients must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func updateAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./updateanypatients%28_,callbackqueue,completion%29-2qqhk.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/updateanypatients(_:callbackqueue:completion:))*