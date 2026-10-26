---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatient"
framework: "CareKit/CareKitStore"
---

# OCKAnyPatient

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Conforming a type to `OCKAnyPatient` allows it to be queried and displayed by CareKit.

## Declaration

```swift
protocol OCKAnyPatient : Sendable
```

## Topics

### Instance Properties
- [var allergies: [String]?](./ockanypatient/allergies.md)
  A list of substances this patient is allergic to.
- [var birthday: Date?](./ockanypatient/birthday.md)
  The patient’s birthday, used to compute their age.
- [var effectiveDate: Date](./ockanypatient/effectivedate.md)
  A date specifying when this version of the patient begins taking effect.
- [var groupIdentifier: String?](./ockanypatient/groupidentifier.md)
  An identifier that can be used to group this patient with others.
- [var id: String](./ockanypatient/id.md)
  A user-defined unique identifier, typically human readable.
- [var name: PersonNameComponents](./ockanypatient/name.md)
  The patient’s name.
- [var notes: [OCKNote]?](./ockanypatient/notes.md)
  Any array of notes associated with this object.
- [var remoteID: String?](./ockanypatient/remoteid.md)
  An identifier for this patient in a remote store.
- [var sex: OCKBiologicalSex?](./ockanypatient/sex.md)
  The patient’s biological sex.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKPatient](./ockpatient.md)

## See Also

### Patients
- [struct OCKPatient](./ockpatient.md)
  Represents a patient
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatient)*