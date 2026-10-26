---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore"
framework: "CareKit/CareKitStore"
---

# OCKPatientStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store that can perform read and write operations on a single type conforming to `OCKAnyPatient` is considered an `OCKPatientStore`.

## Declaration

```swift
protocol OCKPatientStore : OCKAnyPatientStore, OCKReadablePatientStore
```

## Topics

### Instance Methods
- [func addPatient(Patient) async throws -> Patient](./ockpatientstore/addpatient%28_%29.md)
  `addPatient` asynchronously adds a patient to the store.
- [func addPatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./ockpatientstore/addpatient%28_,callbackqueue,completion%29.md)
  `addPatient` asynchronously adds a patient to the store.
- [func addPatients([Patient]) async throws -> [Patient]](./ockpatientstore/addpatients%28_%29.md)
  `addPatients` asynchronously adds an array of patients to the store.
- [func addPatients([Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)](./ockpatientstore/addpatients%28_,callbackqueue,completion%29.md)
  `addPatients` asynchronously adds an array of patients to the store.
- [func deletePatient(Patient) async throws -> Patient](./ockpatientstore/deletepatient%28_%29.md)
  `deletePatient` asynchronously deletes a patient from the store.
- [func deletePatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./ockpatientstore/deletepatient%28_,callbackqueue,completion%29.md)
  `deletePatient` asynchronously deletes a patient from the store.
- [func deletePatients([Patient]) async throws -> [Patient]](./ockpatientstore/deletepatients%28_%29.md)
  `deletePatients` asynchronously deletes an array of patients from the store.
- [func deletePatients([Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)](./ockpatientstore/deletepatients%28_,callbackqueue,completion%29.md)
  `deletePatients` asynchronously deletes an array of patients from the store.
- [func updatePatient(Patient) async throws -> Patient](./ockpatientstore/updatepatient%28_%29.md)
  `updatePatient` asynchronously updates a patient in the store.
- [func updatePatient(Patient, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>?)](./ockpatientstore/updatepatient%28_,callbackqueue,completion%29.md)
  `updatePatient` asynchronously updates a patient in the store.
- [func updatePatients([Patient]) async throws -> [Patient]](./ockpatientstore/updatepatients%28_%29.md)
  `updatePatients` asynchronously updates an array of patients in the store.
- [func updatePatients([Patient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>?)](./ockpatientstore/updatepatients%28_,callbackqueue,completion%29.md)
  `updatePatients` asynchronously updates an array of patients in the store.

## Relationships

### Inherits From
- [OCKAnyPatientStore](./ockanypatientstore.md)
- [OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKReadablePatientStore](./ockreadablepatientstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKStore](./ockstore.md)

## See Also

### Patients
- [struct OCKPatient](./ockpatient.md)
  Represents a patient
- [protocol OCKAnyPatient](./ockanypatient.md)
  Conforming a type to `OCKAnyPatient` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyPatientStore](./ockanypatientstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyPatient` is considered an `OCKAnyPatientStore`.
- [protocol OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
  A store that allows for reading patients.
- [protocol OCKReadablePatientStore](./ockreadablepatientstore.md)
  A store that allows for reading patients.
- [struct OCKPatientQuery](./ockpatientquery.md)
  A query that limits which patients will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore)*