---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/addanypatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyPatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addAnyPatient` asynchronously adds a single patient to the store.

## Declaration

```swift
func addAnyPatient(_ patient: OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)
```

## Parameters

- `patient`: A single patient to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func addAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./addanypatient%28_,callbackqueue,completion%29-7ltt3.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/addanypatient(_:callbackqueue:completion:))*