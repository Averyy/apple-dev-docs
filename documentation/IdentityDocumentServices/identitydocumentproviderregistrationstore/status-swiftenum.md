# IdentityDocumentProviderRegistrationStore.Status

**Framework**: IdentityDocumentServices  
**Kind**: enum

Defines a status for the registration store.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Status
```

#### Discussion

This value indicates whether the app is able to register documents with the system.

## Topics

### Enumeration Cases
- [IdentityDocumentProviderRegistrationStore.Status.authorized](identitydocumentproviderregistrationstore/status-swift.enum/authorized.md)
  The user has authorized the current app for document providing.
- [IdentityDocumentProviderRegistrationStore.Status.notAuthorized](identitydocumentproviderregistrationstore/status-swift.enum/notauthorized.md)
  The user has not yet authorized the current app for document providing.
- [IdentityDocumentProviderRegistrationStore.Status.notDetermined](identitydocumentproviderregistrationstore/status-swift.enum/notdetermined.md)
  The user has not made a choice in to the current app for document providing.
- [IdentityDocumentProviderRegistrationStore.Status.notSupported](identitydocumentproviderregistrationstore/status-swift.enum/notsupported.md)
  The current platform is not supported for document providing.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: IdentityDocumentProviderRegistrationStore.Status](identitydocumentproviderregistrationstore/status-swift.property.md)
  The status of the registration store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/status-swift.enum)*