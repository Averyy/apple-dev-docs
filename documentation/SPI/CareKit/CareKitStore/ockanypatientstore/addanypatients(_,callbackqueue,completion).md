---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/addanypatients(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyPatients(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addAnyPatients` asynchronously adds an array of patients to the store.

## Declaration

```swift
func addAnyPatients(_ patients: [OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)
```

## Parameters

- `patients`: An array of patients to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func addAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./addanypatients%28_,callbackqueue,completion%29-4mjnu.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/addanypatients(_:callbackqueue:completion:))*