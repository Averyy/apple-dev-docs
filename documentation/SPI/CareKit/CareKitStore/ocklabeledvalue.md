---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocklabeledvalue"
framework: "CareKit/CareKitStore"
---

# OCKLabeledValue

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An optional label paired with a value used to represent contact information. The label will typically indicate what kind of information the value carries.

## Declaration

```swift
struct OCKLabeledValue
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ocklabeledvalue/init%28from%29.md)
- [init(label: String, value: String)](./ocklabeledvalue/init%28label,value%29.md)
  Initialize with an optional label and a value.
### Instance Properties
- [var label: String](./ocklabeledvalue/label.md)
  A description of what the label is, i.e. “Home Email”, “Office Phone”
- [var value: String](./ocklabeledvalue/value.md)
  The actual contact information, i.e. a phone number or email address.
### Default Implementations
- [Equatable Implementations](./ocklabeledvalue/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocklabeledvalue)*