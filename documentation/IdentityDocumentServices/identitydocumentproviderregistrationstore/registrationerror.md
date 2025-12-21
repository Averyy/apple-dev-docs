# IdentityDocumentProviderRegistrationStore.RegistrationError

**Framework**: IdentityDocumentServices  
**Kind**: enum

An error type that the identity document registration store and associated types throw.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum RegistrationError
```

## Topics

### Enumeration Cases
- [IdentityDocumentProviderRegistrationStore.RegistrationError.invalidRequest](identitydocumentproviderregistrationstore/registrationerror/invalidrequest.md)
  An error that indicates the request isn’t valid.
- [IdentityDocumentProviderRegistrationStore.RegistrationError.notAuthorized](identitydocumentproviderregistrationstore/registrationerror/notauthorized.md)
  An error that indicates the device is not authorized to interact with the identity document provider registration store.
- [IdentityDocumentProviderRegistrationStore.RegistrationError.notSupported](identitydocumentproviderregistrationstore/registrationerror/notsupported.md)
  An error that indicates that the system cannot register the identity documents on the current platform.
- [IdentityDocumentProviderRegistrationStore.RegistrationError.unknown](identitydocumentproviderregistrationstore/registrationerror/unknown.md)
  An error that indicates the framework encountered a problem which the system can’t interpret.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/registrationerror)*