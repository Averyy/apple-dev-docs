---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientquery"
framework: "CareKit/CareKitStore"
---

# OCKPatientQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which patients will be returned when fetching.

## Declaration

```swift
struct OCKPatientQuery
```

## Topics

### Initializers
- [init(dateInterval: DateInterval?)](./ockpatientquery/init%28dateinterval%29.md)
- [init(for: Date)](./ockpatientquery/init%28for%29.md)
  Create a query with that spans the entire day on the date given.
- [init(id: String)](./ockpatientquery/init%28id%29.md)
### Instance Properties
- [var dateInterval: DateInterval?](./ockpatientquery/dateinterval.md)
- [var groupIdentifiers: [String?]](./ockpatientquery/groupidentifiers.md)
- [var ids: [String]](./ockpatientquery/ids.md)
- [var limit: Int?](./ockpatientquery/limit.md)
- [var offset: Int](./ockpatientquery/offset.md)
- [var remoteIDs: [String?]](./ockpatientquery/remoteids.md)
- [var sortDescriptors: [SortDescriptor]](./ockpatientquery/sortdescriptors.md)
  The order in which the results will be sorted when returned from the query.
- [var tags: [String]](./ockpatientquery/tags.md)
- [var uuids: [UUID]](./ockpatientquery/uuids.md)
### Enumerations
- [OCKPatientQuery.SortDescriptor](./ockpatientquery/sortdescriptor.md)
  Specifies the order in which query results will be sorted.
### Default Implementations
- [Equatable Implementations](./ockpatientquery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

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
- [protocol OCKReadablePatientStore](./ockreadablepatientstore.md)
  A store that allows for reading patients.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientquery)*