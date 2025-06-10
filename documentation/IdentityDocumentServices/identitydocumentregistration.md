# IdentityDocumentRegistration

**Framework**: IdentityDocumentServices  
**Kind**: protocol

A protocol that defines an identity document registration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
protocol IdentityDocumentRegistration : Sendable
```

#### Discussion

Each kind of document format needs its own concrete type that conforms to this protocol.

## Topics

### Instance Properties
- [var documentIdentifier: String](identitydocumentregistration/documentidentifier.md)
  An identifier that uniquely refers to the required document.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [MobileDocumentRegistration](mobiledocumentregistration.md)

## See Also

- [actor IdentityDocumentProviderRegistrationStore](identitydocumentproviderregistrationstore.md)
  A store that notifies the system which documents an app has available for presentment.
- [struct MobileDocumentRegistration](mobiledocumentregistration.md)
  A type you use to register mobile documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentregistration)*