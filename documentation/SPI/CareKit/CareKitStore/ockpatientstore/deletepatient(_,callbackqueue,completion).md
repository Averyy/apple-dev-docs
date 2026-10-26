---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deletePatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deletePatient` asynchronously deletes a patient from the store.

## Declaration

```swift
func deletePatient(_ patient: Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)
```

## Parameters

- `patient`: A patient to be deleted. The patient must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKPatientStore Implementations
- [func deletePatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./deletepatient%28_,callbackqueue,completion%29-4tzcg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatient(_:callbackqueue:completion:))*