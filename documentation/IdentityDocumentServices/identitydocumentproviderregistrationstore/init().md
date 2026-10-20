# init()

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes an identity document provider registration store.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
init()
```

## See Also

### Registering and removing mobile documents
- [func addRegistration(some IdentityDocumentRegistration) async throws](./addregistration%28_%29.md)
  Register a document with the system.
- [var registrations: [any IdentityDocumentRegistration]](./registrations.md)
  A list of all documents registered with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](./removeregistration%28fordocumentidentifier%29.md)
  Unregister a specific document with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/init())*