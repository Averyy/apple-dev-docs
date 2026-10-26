---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablepatientstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadablePatientStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func fetchPatient(withID: String) async throws -> Patient](./fetchpatient%28withid%29.md)
  `fetchPatient` asynchronously fetches a single patient from the store using its user-defined identifier. If a patient with the specified identifier does not exist, the completion handler will be called with an error.
- [func fetchPatient(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>)](./fetchpatient%28withid,callbackqueue,completion%29.md)
- [func fetchPatients(query: OCKPatientQuery) async throws -> [Patient]](./fetchpatients%28query%29.md)
  `fetchPatients` asynchronously retrieves an array of patients from the store.
- [func fetchPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKPatient], OCKStoreError>) -> Void)](./fetchpatients%28query,callbackqueue,completion%29.md)
- [func patients(matching: OCKPatientQuery) -> some AsyncSequence<[OCKPatient], Error> & Sendable](./patients%28matching%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablepatientstore-implementations)*