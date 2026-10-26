---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontact"
framework: "CareKit/CareKitStore"
---

# OCKAnyContact

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Conforming a type to `OCKAnyContact` allows it to be queried and displayed by CareKit.

## Declaration

```swift
protocol OCKAnyContact : Sendable
```

## Topics

### Instance Properties
- [var address: OCKPostalAddress?](./ockanycontact/address.md)
  The contact’s postal address.
- [var asset: String?](./ockanycontact/asset.md)
  A string representation of an asset.
- [var category: OCKContactCategory?](./ockanycontact/category.md)
  Indicates if this contact is care provider or if they are a friend or family member.
- [var effectiveDate: Date](./ockanycontact/effectivedate.md)
  A date specifying when this version of the contact begins taking effect.
- [var emailAddresses: [OCKLabeledValue]?](./ockanycontact/emailaddresses.md)
  An array of the contact’s email addresses.
- [var groupIdentifier: String?](./ockanycontact/groupidentifier.md)
  An identifier that can be used to group this contact with others.
- [var id: String](./ockanycontact/id.md)
  A user-defined unique identifier, typically human readable.
- [var messagingNumbers: [OCKLabeledValue]?](./ockanycontact/messagingnumbers.md)
  An array of numbers that the contact can be messaged at. The number strings may contains non-numeric characters.
- [var name: PersonNameComponents](./ockanycontact/name.md)
  The contact’s name.
- [var notes: [OCKNote]?](./ockanycontact/notes.md)
  Any array of notes associated with this object.
- [var organization: String?](./ockanycontact/organization.md)
  The organization this contact belongs to.
- [var otherContactInfo: [OCKLabeledValue]?](./ockanycontact/othercontactinfo.md)
  An array of other information that could be used reach this contact.
- [var phoneNumbers: [OCKLabeledValue]?](./ockanycontact/phonenumbers.md)
  An array of the contact’s phone numbers. The number strings may contains non-numeric characters.
- [var remoteID: String?](./ockanycontact/remoteid.md)
  An identifier for this contact in a remote store.
- [var role: String?](./ockanycontact/role.md)
  A description of what this contact’s role is.
- [var title: String?](./ockanycontact/title.md)
  A title for this contact.
### Instance Methods
- [func belongs(to: OCKAnyCarePlan) -> Bool](./ockanycontact/belongs%28to%29.md)
  Determines if this contact belongs to the given care plan.
- [func isEqual(to: OCKAnyContact) -> Bool](./ockanycontact/isequal%28to%29.md)
  Determines if this contact equals another contact.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKContact](./ockcontact.md)

## See Also

### Contacts
- [struct OCKContact](./ockcontact.md)
  An `OCKContact` represents a contact that a user may want to get in touch with. A contact may be a care provider, a friend, or a family member. Contacts must have at least a name, and may optionally have numerous other addresses at which to be contacted.
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
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontact)*