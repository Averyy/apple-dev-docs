---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/addpatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addPatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addPatient` asynchronously adds a patient to the store.

## Declaration

```swift
func addPatient(_ patient: Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)
```

## Parameters

- `patient`: A patient to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKPatientStore Implementations
- [func addPatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./addpatient%28_,callbackqueue,completion%29-8rq3i.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/addpatient(_:callbackqueue:completion:))*