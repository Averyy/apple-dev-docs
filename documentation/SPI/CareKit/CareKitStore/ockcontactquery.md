---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactquery"
framework: "CareKit/CareKitStore"
---

# OCKContactQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which contacts will be returned when fetching.

## Declaration

```swift
struct OCKContactQuery
```

## Topics

### Initializers
- [init()](./ockcontactquery/init%28%29.md)
- [init(dateInterval: DateInterval?)](./ockcontactquery/init%28dateinterval%29.md)
- [init(for: Date)](./ockcontactquery/init%28for%29.md)
  Create a query with that spans the entire day on the date given.
- [init(id: String)](./ockcontactquery/init%28id%29.md)
### Instance Properties
- [var carePlanIDs: [String]](./ockcontactquery/careplanids.md)
  The identifiers of care plans to match against.
- [var carePlanRemoteIDs: [String]](./ockcontactquery/careplanremoteids.md)
  The remote ID of care plans for which contacts should match.
- [var carePlanUUIDs: [UUID]](./ockcontactquery/careplanuuids.md)
  The version of the care plans for which contacts should match.
- [var dateInterval: DateInterval?](./ockcontactquery/dateinterval.md)
- [var groupIdentifiers: [String?]](./ockcontactquery/groupidentifiers.md)
- [var ids: [String]](./ockcontactquery/ids.md)
- [var limit: Int?](./ockcontactquery/limit.md)
- [var offset: Int](./ockcontactquery/offset.md)
- [var remoteIDs: [String?]](./ockcontactquery/remoteids.md)
- [var sortDescriptors: [SortDescriptor]](./ockcontactquery/sortdescriptors.md)
  The order in which the results will be sorted when returned from the query.
- [var tags: [String]](./ockcontactquery/tags.md)
- [var uuids: [UUID]](./ockcontactquery/uuids.md)
### Enumerations
- [OCKContactQuery.SortDescriptor](./ockcontactquery/sortdescriptor.md)
  Specifies the order in which query results will be sorted.
### Default Implementations
- [Equatable Implementations](./ockcontactquery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Contacts
- [struct OCKContact](./ockcontact.md)
  An `OCKContact` represents a contact that a user may want to get in touch with. A contact may be a care provider, a friend, or a family member. Contacts must have at least a name, and may optionally have numerous other addresses at which to be contacted.
- [protocol OCKAnyContact](./ockanycontact.md)
  Conforming a type to `OCKAnyContact` allows it to be queried and displayed by CareKit.
- [struct OCKPostalAddress](./ockpostaladdress.md)
  A representation of the postal address for a contact.
- [enum OCKBiologicalSex](./ockbiologicalsex.md)
  Represents a person’s biological sex.
- [enum OCKContactCategory](./ockcontactcategory.md)
  An enumerator specifying which group a contact belongs to.
- [struct OCKLabeledValue](./ocklabeledvalue.md)
  An optional label paired with a value used to represent contact information. The label will typically indicate what kind of information the value carries.
- [protocol OCKContactStore](./ockcontactstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyContact` is considered an `OCKCarePlanStore`.
- [protocol OCKAnyContactStore](./ockanycontactstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyContact` is considered an `OCKAnyContactStore`.
- [protocol OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
  A store that allows for reading contacts.
- [protocol OCKReadableContactStore](./ockreadablecontactstore.md)
  A store that allows for reading contacts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactquery)*