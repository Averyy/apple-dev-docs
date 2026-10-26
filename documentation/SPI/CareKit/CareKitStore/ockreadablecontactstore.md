---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore"
framework: "CareKit/CareKitStore"
---

# OCKReadableContactStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading contacts.

## Declaration

```swift
protocol OCKReadableContactStore : OCKAnyReadOnlyContactStore
```

## Topics

### Associated Types
- [associatedtype Contact : OCKAnyContact, Equatable, Identifiable](./ockreadablecontactstore/contact.md)
- [associatedtype Contacts : Sendable, AsyncSequence](./ockreadablecontactstore/contacts.md)
  An asynchronous sequence that produces contacts.
### Instance Methods
- [func contacts(matching: OCKContactQuery) -> Contacts](./ockreadablecontactstore/contacts%28matching%29.md)
  A continuous stream of contacts that exist in the store.
- [func fetchContact(withID: String) async throws -> Contact](./ockreadablecontactstore/fetchcontact%28withid%29.md)
  `fetchContact` asynchronously retrieves a contact from the store using its user-defined unique identifier. If a contact with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchContact(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>)](./ockreadablecontactstore/fetchcontact%28withid,callbackqueue,completion%29.md)
  `fetchContact` asynchronously retrieves a contact from the store using its user-defined unique identifier. If a contact with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchContacts(query: OCKContactQuery) async throws -> [Contact]](./ockreadablecontactstore/fetchcontacts%28query%29.md)
  `fetchContacts` asynchronously retrieves an array of contacts from the store.
- [func fetchContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>)](./ockreadablecontactstore/fetchcontacts%28query,callbackqueue,completion%29.md)
  `fetchContacts` asynchronously retrieves an array of contacts from the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKContactStore](./ockcontactstore.md)
### Conforming Types
- [OCKStore](./ockstore.md)

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
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore)*