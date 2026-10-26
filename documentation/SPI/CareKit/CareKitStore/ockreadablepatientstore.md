---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore"
framework: "CareKit/CareKitStore"
---

# OCKReadablePatientStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading patients.

## Declaration

```swift
protocol OCKReadablePatientStore : OCKAnyReadOnlyPatientStore
```

## Topics

### Associated Types
- [associatedtype Patient : OCKAnyPatient, Equatable, Identifiable](./ockreadablepatientstore/patient.md)
- [associatedtype Patients : Sendable, AsyncSequence](./ockreadablepatientstore/patients.md)
  An asynchronous sequence that produces patients.
### Instance Methods
- [func fetchPatient(withID: String) async throws -> Patient](./ockreadablepatientstore/fetchpatient%28withid%29.md)
  `fetchPatient` asynchronously fetches a single patient from the store using its user-defined identifier. If a patient with the specified identifier does not exist, the completion handler will be called with an error.
- [func fetchPatient(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>)](./ockreadablepatientstore/fetchpatient%28withid,callbackqueue,completion%29.md)
  `fetchPatient` asynchronously fetches a single patient from the store using its user-defined identifier. If a patient with the specified identifier does not exist, the completion handler will be called with an error.
- [func fetchPatients(query: OCKPatientQuery) async throws -> [Patient]](./ockreadablepatientstore/fetchpatients%28query%29.md)
  `fetchPatients` asynchronously retrieves an array of patients from the store.
- [func fetchPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Patient]>)](./ockreadablepatientstore/fetchpatients%28query,callbackqueue,completion%29.md)
  `fetchPatients` asynchronously retrieves an array of patients from the store.
- [func patients(matching: OCKPatientQuery) -> Patients](./ockreadablepatientstore/patients%28matching%29.md)
  A continuous stream of patients that exist in the store.

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
- [protocol OCKPatientStore](./ockpatientstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyPatient` is considered an `OCKPatientStore`.
- [struct OCKPatientQuery](./ockpatientquery.md)
  A query that limits which patients will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore)*