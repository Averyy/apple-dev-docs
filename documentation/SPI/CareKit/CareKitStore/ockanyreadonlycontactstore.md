---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyContactStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading contacts.

## Declaration

```swift
protocol OCKAnyReadOnlyContactStore : OCKAnyResettableStore
```

## Topics

### Instance Methods
- [func anyContacts(matching: OCKContactQuery) -> CareStoreQueryResults<OCKAnyContact>](./ockanyreadonlycontactstore/anycontacts%28matching%29.md)
  A continuous stream of contacts that exist in the store.
- [func fetchAnyContact(withID: String) async throws -> OCKAnyContact](./ockanyreadonlycontactstore/fetchanycontact%28withid%29.md)
  `fetchAnyContact` asynchronously retrieves a single contact from the store.
- [func fetchAnyContact(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>)](./ockanyreadonlycontactstore/fetchanycontact%28withid,callbackqueue,completion%29.md)
  `fetchAnyContact` asynchronously retrieves a single contact from the store.
- [func fetchAnyContacts(query: OCKContactQuery) async throws -> [OCKAnyContact]](./ockanyreadonlycontactstore/fetchanycontacts%28query%29.md)
  `fetchAnyContacts` asynchronously retrieves an array of contacts from the store.
- [func fetchAnyContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>)](./ockanyreadonlycontactstore/fetchanycontacts%28query,callbackqueue,completion%29.md)
  `fetchAnyContacts` asynchronously retrieves an array of contacts from the store.

## Relationships

### Inherits From
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyContactStore](./ockanycontactstore.md)
- [OCKContactStore](./ockcontactstore.md)
- [OCKReadableContactStore](./ockreadablecontactstore.md)
### Conforming Types
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

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
- [protocol OCKReadableContactStore](./ockreadablecontactstore.md)
  A store that allows for reading contacts.
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore)*