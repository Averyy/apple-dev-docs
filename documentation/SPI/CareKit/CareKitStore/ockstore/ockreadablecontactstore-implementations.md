---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablecontactstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadableContactStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func contacts(matching: OCKContactQuery) -> some AsyncSequence<[OCKContact], Error> & Sendable](./contacts%28matching%29.md)
- [func fetchContact(withID: String) async throws -> Contact](./fetchcontact%28withid%29.md)
  `fetchContact` asynchronously retrieves a contact from the store using its user-defined unique identifier. If a contact with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchContact(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>)](./fetchcontact%28withid,callbackqueue,completion%29.md)
- [func fetchContacts(query: OCKContactQuery) async throws -> [Contact]](./fetchcontacts%28query%29.md)
  `fetchContacts` asynchronously retrieves an array of contacts from the store.
- [func fetchContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKContact], OCKStoreError>) -> Void)](./fetchcontacts%28query,callbackqueue,completion%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablecontactstore-implementations)*