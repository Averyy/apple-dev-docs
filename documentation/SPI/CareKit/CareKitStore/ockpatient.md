---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatient"
framework: "CareKit/CareKitStore"
---

# OCKPatient

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

Represents a patient

## Declaration

```swift
struct OCKPatient
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockpatient/init%28from%29.md)
- [init(id: String, givenName: String, familyName: String)](./ockpatient/init%28id,givenname,familyname%29.md)
  Initialize a patient with an id, a first name, and a last name.
- [init(id: String, name: PersonNameComponents)](./ockpatient/init%28id,name%29.md)
  Initialize a new patient with an id and a name.
### Instance Properties
- [var age: Int?](./ockpatient/age.md)
  The patient’s age in years, as of the current date.
- [var allergies: [String]?](./ockpatient/allergies.md)
- [var asset: String?](./ockpatient/asset.md)
- [var birthday: Date?](./ockpatient/birthday.md)
- [var createdDate: Date?](./ockpatient/createddate.md)
- [var deletedDate: Date?](./ockpatient/deleteddate.md)
- [var effectiveDate: Date](./ockpatient/effectivedate.md)
- [var groupIdentifier: String?](./ockpatient/groupidentifier.md)
- [var id: String](./ockpatient/id.md)
- [var name: PersonNameComponents](./ockpatient/name.md)
- [var nextVersionUUIDs: [UUID]](./ockpatient/nextversionuuids.md)
- [var notes: [OCKNote]?](./ockpatient/notes.md)
- [var previousVersionUUIDs: [UUID]](./ockpatient/previousversionuuids.md)
- [var remoteID: String?](./ockpatient/remoteid.md)
- [var schemaVersion: OCKSemanticVersion?](./ockpatient/schemaversion.md)
- [var sex: OCKBiologicalSex?](./ockpatient/sex.md)
- [var source: String?](./ockpatient/source.md)
- [var tags: [String]?](./ockpatient/tags.md)
- [var timezone: TimeZone](./ockpatient/timezone.md)
- [var updatedDate: Date?](./ockpatient/updateddate.md)
- [var userInfo: [String : String]?](./ockpatient/userinfo.md)
- [var uuid: UUID](./ockpatient/uuid.md)
### Default Implementations
- [Equatable Implementations](./ockpatient/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyPatient](./ockanypatient.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Patients
- [protocol OCKAnyPatient](./ockanypatient.md)
  Conforming a type to `OCKAnyPatient` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyPatientStore](./ockanypatientstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyPatient` is considered an `OCKAnyPatientStore`.
- [protocol OCKAnyReadOnlyPatientStore](./ockanyreadonlypatientstore.md)
  A store that allows for reading patients.
- [protocol OCKPatientStore](./ockpatientstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyPatient` is considered an `OCKPatientStore`.
- [protocol OCKReadablePatientStore](./ockreadablepatientstore.md)
  A store that allows for reading patients.
- [struct OCKPatientQuery](./ockpatientquery.md)
  A query that limits which patients will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatient)*