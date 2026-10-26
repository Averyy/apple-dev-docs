---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyPatientStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading patients.

## Declaration

```swift
protocol OCKAnyReadOnlyPatientStore : OCKAnyResettableStore
```

## Topics

### Instance Methods
- [func anyPatients(matching: OCKPatientQuery) -> CareStoreQueryResults<OCKAnyPatient>](./ockanyreadonlypatientstore/anypatients%28matching%29.md)
  A continuous stream of patients that exist in the store.
- [func fetchAnyPatient(withID: String) async throws -> OCKAnyPatient](./ockanyreadonlypatientstore/fetchanypatient%28withid%29.md)
  `fetchAnyPatient` asynchronously retrieves a single patient from the store.
- [func fetchAnyPatient(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>)](./ockanyreadonlypatientstore/fetchanypatient%28withid,callbackqueue,completion%29.md)
  `fetchAnyPatient` asynchronously retrieves a single patient from the store.
- [func fetchAnyPatients(query: OCKPatientQuery) async throws -> [OCKAnyPatient]](./ockanyreadonlypatientstore/fetchanypatients%28query%29.md)
  `fetchAnyPatients` asynchronously retrieves an array of patients from the store.
- [func fetchAnyPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>)](./ockanyreadonlypatientstore/fetchanypatients%28query,callbackqueue,completion%29.md)
  `fetchAnyPatients` asynchronously retrieves an array of patients from the store.

## Relationships

### Inherits From
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyPatientStore](./ockanypatientstore.md)
- [OCKPatientStore](./ockpatientstore.md)
- [OCKReadablePatientStore](./ockreadablepatientstore.md)
### Conforming Types
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

## See Also

### Patients
- [struct OCKPatient](./ockpatient.md)
  Represents a patient
- [protocol OCKAnyPatient](./ockanypatient.md)
  Conforming a type to `OCKAnyPatient` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyPatientStore](./ockanypatientstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyPatient` is considered an `OCKAnyPatientStore`.
- [protocol OCKPatientStore](./ockpatientstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyPatient` is considered an `OCKPatientStore`.
- [protocol OCKReadablePatientStore](./ockreadablepatientstore.md)
  A store that allows for reading patients.
- [struct OCKPatientQuery](./ockpatientquery.md)
  A query that limits which patients will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore)*