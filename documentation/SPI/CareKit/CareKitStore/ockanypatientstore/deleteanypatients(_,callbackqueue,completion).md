---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/deleteanypatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyPatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteAnyPatients` asynchronously deletes an array of patients from the store.

## Declaration

```swift
func deleteAnyPatients(_ patients: [OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)
```

## Parameters

- `patients`: An array of patients to be deleted. The patients must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func deleteAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./deleteanypatients%28_,callbackqueue,completion%29-443of.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/deleteanypatients(_:callbackqueue:completion:))*