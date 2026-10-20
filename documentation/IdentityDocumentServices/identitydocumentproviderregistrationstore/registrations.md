# registrations

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A list of all documents registered with the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
var registrations: [any IdentityDocumentRegistration] { get async throws }
```

## See Also

### Registering and removing mobile documents
- [init()](./init%28%29.md)
  Initializes an identity document provider registration store.
- [func addRegistration(some IdentityDocumentRegistration) async throws](./addregistration%28_%29.md)
  Register a document with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](./removeregistration%28fordocumentidentifier%29.md)
  Unregister a specific document with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/registrations)*