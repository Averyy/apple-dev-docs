# init()

**Framework**: IdentityDocumentServices  
**Kind**: init

Initializes an identity document provider registration store.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init()
```

## See Also

- [func addRegistration(some IdentityDocumentRegistration) async throws](identitydocumentproviderregistrationstore/addregistration(_:).md)
  Register a document with the system.
- [var registrations: [any IdentityDocumentRegistration]](identitydocumentproviderregistrationstore/registrations.md)
  A list of all documents registered with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](identitydocumentproviderregistrationstore/removeregistration(fordocumentidentifier:).md)
  Unregister a specific document with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/init())*