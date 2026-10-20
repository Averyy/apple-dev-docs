# addRegistration(_:)

**Framework**: IdentityDocumentServices  
**Kind**: method

Register a document with the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
func addRegistration(_ registration: some IdentityDocumentRegistration) async throws
```

#### Discussion

If the provided registration contains a `documentIdentifier` that is already registered, the system replaces the existing registration with the provided registration.

## Parameters

- `registration`: A registration that contains information about the document necessary to surface it appropriately during a presentment.

## See Also

- [init()](identitydocumentproviderregistrationstore/init.md)
  Initializes an identity document provider registration store.
- [var registrations: [any IdentityDocumentRegistration]](identitydocumentproviderregistrationstore/registrations.md)
  A list of all documents registered with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](identitydocumentproviderregistrationstore/removeregistration(fordocumentidentifier:).md)
  Unregister a specific document with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/addregistration(_:))*