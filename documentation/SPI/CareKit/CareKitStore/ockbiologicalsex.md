---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockbiologicalsex"
framework: "CareKit/CareKitStore"
---

# OCKBiologicalSex

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

Represents a person’s biological sex.

## Declaration

```swift
enum OCKBiologicalSex
```

## Topics

### Enumeration Cases
- [OCKBiologicalSex.female](./ockbiologicalsex/female.md)
- [OCKBiologicalSex.male](./ockbiologicalsex/male.md)
- [OCKBiologicalSex.other(_:)](./ockbiologicalsex/other%28_%29.md)
### Initializers
- [init(from: Decoder) throws](./ockbiologicalsex/init%28from%29.md)
- [init?(rawValue: String)](./ockbiologicalsex/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: String](./ockbiologicalsex/rawvalue.md)
### Instance Methods
- [func encode(to: Encoder) throws](./ockbiologicalsex/encode%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockbiologicalsex/equatable-implementations.md)
- [RawRepresentable Implementations](./ockbiologicalsex/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
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
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockbiologicalsex)*