# MobileDocumentRegistration

**Framework**: IdentityDocumentServices  
**Kind**: struct

A type you use to register mobile documents.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct MobileDocumentRegistration
```

#### Overview

Mobile documents, or “mdocs”, are a document format defined in ISO 18013-5.

## Topics

### Initializers
- [init(mobileDocumentType: String, supportedAuthorityKeyIdentifiers: [Data], documentIdentifier: String, invalidationDate: Date?)](mobiledocumentregistration/init(mobiledocumenttype:supportedauthoritykeyidentifiers:documentidentifier:invalidationdate:).md)
  Initializes a mobile document registration.
### Instance Properties
- [var documentIdentifier: String](mobiledocumentregistration/documentidentifier.md)
  An identifier that uniquely refers to the registered document.
- [var invalidationDate: Date?](mobiledocumentregistration/invalidationdate.md)
  A date that indicates when the system needs to invalidate this registration.
- [var mobileDocumentType: String](mobiledocumentregistration/mobiledocumenttype.md)
  The type of the mobile document.
- [var supportedAuthorityKeyIdentifiers: [Data]](mobiledocumentregistration/supportedauthoritykeyidentifiers.md)
  A list of authority key identifiers that correspond to relying party authorizers that are trusted by the document provider app.

## Relationships

### Conforms To
- [IdentityDocumentRegistration](identitydocumentregistration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor IdentityDocumentProviderRegistrationStore](identitydocumentproviderregistrationstore.md)
  A store that notifies the system which documents an app has available for presentment.
- [protocol IdentityDocumentRegistration](identitydocumentregistration.md)
  A protocol that defines an identity document registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration)*