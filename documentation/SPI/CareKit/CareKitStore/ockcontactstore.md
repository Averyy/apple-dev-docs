---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore"
framework: "CareKit/CareKitStore"
---

# OCKContactStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store that can perform read and write operations on a single type conforming to `OCKAnyContact` is considered an `OCKCarePlanStore`.

## Declaration

```swift
protocol OCKContactStore : OCKAnyContactStore, OCKReadableContactStore
```

## Topics

### Instance Methods
- [func addContact(Contact) async throws -> Contact](./ockcontactstore/addcontact%28_%29.md)
  `addContact` asynchronously adds a contact to the store.
- [func addContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./ockcontactstore/addcontact%28_,callbackqueue,completion%29.md)
  `addContact` asynchronously adds a contact to the store.
- [func addContacts([Contact]) async throws -> [Contact]](./ockcontactstore/addcontacts%28_%29.md)
  `addContacts` asynchronously adds an array of contacts to the store.
- [func addContacts([Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)](./ockcontactstore/addcontacts%28_,callbackqueue,completion%29.md)
  `addContacts` asynchronously adds an array of contacts to the store.
- [func deleteContact(Contact) async throws -> Contact](./ockcontactstore/deletecontact%28_%29.md)
  `deleteContact` asynchronously deletes a contact from the store.
- [func deleteContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./ockcontactstore/deletecontact%28_,callbackqueue,completion%29.md)
  `deleteContact` asynchronously deletes a contact from the store.
- [func deleteContacts([Contact]) async throws -> [Contact]](./ockcontactstore/deletecontacts%28_%29.md)
  `deleteContacts` asynchronously deletes an array of contacts from the store.
- [func deleteContacts([Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)](./ockcontactstore/deletecontacts%28_,callbackqueue,completion%29.md)
  `deleteContacts` asynchronously deletes an array of contacts from the store.
- [func updateContact(Contact) async throws -> Contact](./ockcontactstore/updatecontact%28_%29.md)
  `updateContact` asynchronously updates a contacts in the store.
- [func updateContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./ockcontactstore/updatecontact%28_,callbackqueue,completion%29.md)
  `updateContact` asynchronously updates a contacts in the store.
- [func updateContacts([Contact]) async throws -> [Contact]](./ockcontactstore/updatecontacts%28_%29.md)
  `updateContacts` asynchronously updates an array of contacts in the store.
- [func updateContacts([Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)](./ockcontactstore/updatecontacts%28_,callbackqueue,completion%29.md)
  `updateContacts` asynchronously updates an array of contacts in the store.

## Relationships

### Inherits From
- [OCKAnyContactStore](./ockanycontactstore.md)
- [OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKReadableContactStore](./ockreadablecontactstore.md)
- Swift.Sendable
- Swift.SendableMetatype
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
- [protocol OCKAnyContactStore](./ockanycontactstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyContact` is considered an `OCKAnyContactStore`.
- [protocol OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
  A store that allows for reading contacts.
- [protocol OCKReadableContactStore](./ockreadablecontactstore.md)
  A store that allows for reading contacts.
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore)*