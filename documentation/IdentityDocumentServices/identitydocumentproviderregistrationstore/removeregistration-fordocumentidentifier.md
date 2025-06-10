# removeRegistration(forDocumentIdentifier:)

**Framework**: IdentityDocumentServices  
**Kind**: method

Unregister a specific document with the system.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func removeRegistration(forDocumentIdentifier documentIdentifier: String) async throws
```

#### Discussion

When a document is unregistered, the system no longer surfaces your app as an option for responding to a presentment request for that specific document.

## Parameters

- `documentIdentifier`: The identifier of the document to unregister.

## See Also

- [init()](identitydocumentproviderregistrationstore/init.md)
  Initializes an identity document provider registration store.
- [func addRegistration(some IdentityDocumentRegistration) async throws](identitydocumentproviderregistrationstore/addregistration(_:).md)
  Register a document with the system.
- [var registrations: [any IdentityDocumentRegistration]](identitydocumentproviderregistrationstore/registrations.md)
  A list of all documents registered with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/removeregistration(fordocumentidentifier:))*