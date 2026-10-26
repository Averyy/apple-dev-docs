---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyPatientStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store able to write to one ore more types conforming to `OCKAnyPatient` is considered an `OCKAnyPatientStore`.

## Declaration

```swift
protocol OCKAnyPatientStore : OCKAnyReadOnlyPatientStore
```

## Topics

### Instance Methods
- [func addAnyPatient(OCKAnyPatient) async throws -> OCKAnyPatient](./ockanypatientstore/addanypatient%28_%29.md)
  `addAnyPatient` asynchronously adds a single patient to the store.
- [func addAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./ockanypatientstore/addanypatient%28_,callbackqueue,completion%29.md)
  `addAnyPatient` asynchronously adds a single patient to the store.
- [func addAnyPatients([OCKAnyPatient]) async throws -> [OCKAnyPatient]](./ockanypatientstore/addanypatients%28_%29.md)
  `addAnyPatients` asynchronously adds an array of patients to the store.
- [func addAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./ockanypatientstore/addanypatients%28_,callbackqueue,completion%29.md)
  `addAnyPatients` asynchronously adds an array of patients to the store.
- [func deleteAnyPatient(OCKAnyPatient) async throws -> OCKAnyPatient](./ockanypatientstore/deleteanypatient%28_%29.md)
  `deleteAnyPatient` asynchronously deletes a single patient from the store.
- [func deleteAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./ockanypatientstore/deleteanypatient%28_,callbackqueue,completion%29.md)
  `deleteAnyPatient` asynchronously deletes a single patient from the store.
- [func deleteAnyPatients([OCKAnyPatient]) async throws -> [OCKAnyPatient]](./ockanypatientstore/deleteanypatients%28_%29.md)
  `deleteAnyPatients` asynchronously deletes an array of patients from the store.
- [func deleteAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./ockanypatientstore/deleteanypatients%28_,callbackqueue,completion%29.md)
  `deleteAnyPatients` asynchronously deletes an array of patients from the store.
- [func updateAnyPatient(OCKAnyPatient) async throws -> OCKAnyPatient](./ockanypatientstore/updateanypatient%28_%29.md)
  `updateAnyPatient` asynchronously updates a single patient in the store.
- [func updateAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./ockanypatientstore/updateanypatient%28_,callbackqueue,completion%29.md)
  `updateAnyPatient` asynchronously updates a single patient in the store.
- [func updateAnyPatients([OCKAnyPatient]) async throws -> [OCKAnyPatient]](./ockanypatientstore/updateanypatients%28_%29.md)
  `updateAnyPatients` asynchronously updates an array of patients in the store.
- [func updateAnyPatients([OCKAnyPatient], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>?)](./ockanypatientstore/updateanypatients%28_,callbackqueue,completion%29.md)
  `updateAnyPatients` asynchronously updates an array of patients in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKPatientStore](./ockpatientstore.md)
### Conforming Types
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

## See Also

### Patients
- [struct OCKPatient](./ockpatient.md)
  Represents a patient
- [protocol OCKAnyPatient](./ockanypatient.md)
  Conforming a type to `OCKAnyPatient` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
  A store that allows for reading patients.
- [protocol OCKPatientStore](./ockpatientstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyPatient` is considered an `OCKPatientStore`.
- [protocol OCKReadablePatientStore](./ockreadablepatientstore.md)
  A store that allows for reading patients.
- [struct OCKPatientQuery](./ockpatientquery.md)
  A query that limits which patients will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore)*