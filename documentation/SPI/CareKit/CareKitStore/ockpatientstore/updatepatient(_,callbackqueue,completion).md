---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/updatepatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updatePatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updatePatient` asynchronously updates a patient in the store.

## Declaration

```swift
func updatePatient(_ patient: Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)
```

## Parameters

- `patient`: A patient to be updated. The patient must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKPatientStore Implementations
- [func updatePatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./updatepatient%28_,callbackqueue,completion%29-vs7p.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/updatepatient(_:callbackqueue:completion:))*