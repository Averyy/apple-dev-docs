---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyContactStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store able to write to one ore more types conforming to `OCKAnyContact` is considered an `OCKAnyContactStore`.

## Declaration

```swift
protocol OCKAnyContactStore : OCKAnyReadOnlyContactStore
```

## Topics

### Instance Methods
- [func addAnyContact(OCKAnyContact) async throws -> OCKAnyContact](./ockanycontactstore/addanycontact%28_%29.md)
  `addAnyContact` asynchronously adds a single contact to the store.
- [func addAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./ockanycontactstore/addanycontact%28_,callbackqueue,completion%29.md)
  `addAnyContact` asynchronously adds a single contact to the store.
- [func addAnyContacts([OCKAnyContact]) async throws -> [OCKAnyContact]](./ockanycontactstore/addanycontacts%28_%29.md)
  `addAnyContacts` asynchronously adds an array of contacts to the store.
- [func addAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./ockanycontactstore/addanycontacts%28_,callbackqueue,completion%29.md)
  `addAnyContacts` asynchronously adds an array of contacts to the store.
- [func deleteAnyContact(OCKAnyContact) async throws -> OCKAnyContact](./ockanycontactstore/deleteanycontact%28_%29.md)
  `deleteAnyContact` asynchronously deletes a single contact from the store.
- [func deleteAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./ockanycontactstore/deleteanycontact%28_,callbackqueue,completion%29.md)
  `deleteAnyContact` asynchronously deletes a single contact from the store.
- [func deleteAnyContacts([OCKAnyContact]) async throws -> [OCKAnyContact]](./ockanycontactstore/deleteanycontacts%28_%29.md)
  `deleteAnyContacts` asynchronously deletes an array of contacts from the store.
- [func deleteAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./ockanycontactstore/deleteanycontacts%28_,callbackqueue,completion%29.md)
  `deleteAnyContacts` asynchronously deletes an array of contacts from the store.
- [func updateAnyContact(OCKAnyContact) async throws -> OCKAnyContact](./ockanycontactstore/updateanycontact%28_%29.md)
  `updateAnyContact` asynchronously update a single contact in the store.
- [func updateAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./ockanycontactstore/updateanycontact%28_,callbackqueue,completion%29.md)
  `updateAnyContact` asynchronously update single contact in the store.
- [func updateAnyContacts([OCKAnyContact]) async throws -> [OCKAnyContact]](./ockanycontactstore/updateanycontacts%28_%29.md)
  `updateAnyContacts` asynchronously updates an array of contacts in the store.
- [func updateAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./ockanycontactstore/updateanycontacts%28_,callbackqueue,completion%29.md)
  `updateAnyContacts` asynchronously updates an array of contacts in the store.

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
- [protocol OCKAnyReadOnlyContactStore](./ockanyreadonlycontactstore.md)
  A store that allows for reading contacts.
- [protocol OCKReadableContactStore](./ockreadablecontactstore.md)
  A store that allows for reading contacts.
- [struct OCKContactQuery](./ockcontactquery.md)
  A query that limits which contacts will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore)*