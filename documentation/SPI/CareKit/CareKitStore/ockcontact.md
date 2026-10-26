---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontact"
framework: "CareKit/CareKitStore"
---

# OCKContact

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKContact` represents a contact that a user may want to get in touch with. A contact may be a care provider, a friend, or a family member. Contacts must have at least a name, and may optionally have numerous other addresses at which to be contacted.

## Declaration

```swift
struct OCKContact
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockcontact/init%28from%29.md)
- [init(id: String, givenName: String, familyName: String, carePlanUUID: UUID?)](./ockcontact/init%28id,givenname,familyname,careplanuuid%29.md)
  Initialize a new `OCKContact` with a user-defined id, a name, and an optional care plan version ID.
- [init(id: String, name: PersonNameComponents, carePlanUUID: UUID?)](./ockcontact/init%28id,name,careplanuuid%29.md)
  Initialize a new `OCKContact` with a user-defined id, a name, and an optional care plan version ID.
### Instance Properties
- [var address: OCKPostalAddress?](./ockcontact/address.md)
- [var asset: String?](./ockcontact/asset.md)
- [var carePlanUUID: UUID?](./ockcontact/careplanuuid.md)
  The version id in the local database for the care plan associated with this contact.
- [var category: OCKContactCategory?](./ockcontact/category.md)
- [var createdDate: Date?](./ockcontact/createddate.md)
- [var deletedDate: Date?](./ockcontact/deleteddate.md)
- [var effectiveDate: Date](./ockcontact/effectivedate.md)
- [var emailAddresses: [OCKLabeledValue]?](./ockcontact/emailaddresses.md)
- [var groupIdentifier: String?](./ockcontact/groupidentifier.md)
- [var id: String](./ockcontact/id.md)
- [var messagingNumbers: [OCKLabeledValue]?](./ockcontact/messagingnumbers.md)
- [var name: PersonNameComponents](./ockcontact/name.md)
- [var nextVersionUUIDs: [UUID]](./ockcontact/nextversionuuids.md)
- [var notes: [OCKNote]?](./ockcontact/notes.md)
- [var organization: String?](./ockcontact/organization.md)
- [var otherContactInfo: [OCKLabeledValue]?](./ockcontact/othercontactinfo.md)
- [var phoneNumbers: [OCKLabeledValue]?](./ockcontact/phonenumbers.md)
- [var previousVersionUUIDs: [UUID]](./ockcontact/previousversionuuids.md)
- [var remoteID: String?](./ockcontact/remoteid.md)
- [var role: String?](./ockcontact/role.md)
- [var schemaVersion: OCKSemanticVersion?](./ockcontact/schemaversion.md)
- [var source: String?](./ockcontact/source.md)
- [var tags: [String]?](./ockcontact/tags.md)
- [var timezone: TimeZone](./ockcontact/timezone.md)
- [var title: String?](./ockcontact/title.md)
- [var updatedDate: Date?](./ockcontact/updateddate.md)
- [var userInfo: [String : String]?](./ockcontact/userinfo.md)
- [var uuid: UUID](./ockcontact/uuid.md)
### Instance Methods
- [func belongs(to: OCKAnyCarePlan) -> Bool](./ockcontact/belongs%28to%29.md)
- [func isEqual(to: OCKAnyContact) -> Bool](./ockcontact/isequal%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockcontact/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyContact](./ockanycontact.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Contacts
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
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontact)*