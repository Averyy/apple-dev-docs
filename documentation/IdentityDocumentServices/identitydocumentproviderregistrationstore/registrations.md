# registrations

**Framework**: IdentityDocumentServices  
**Kind**: property

A list of all documents registered with the system.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var registrations: [any IdentityDocumentRegistration] { get async throws }
```

## See Also

- [init()](identitydocumentproviderregistrationstore/init.md)
  Initializes an identity document provider registration store.
- [func addRegistration(some IdentityDocumentRegistration) async throws](identitydocumentproviderregistrationstore/addregistration(_:).md)
  Register a document with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](identitydocumentproviderregistrationstore/removeregistration(fordocumentidentifier:).md)
  Unregister a specific document with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/registrations)*