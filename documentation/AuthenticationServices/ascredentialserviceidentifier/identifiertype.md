# ASCredentialServiceIdentifier.IdentifierType

**Framework**: Authentication Services  
**Kind**: enum

Possible values for the service identifier type.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum IdentifierType
```

## Topics

### Identifier types
- [ASCredentialServiceIdentifier.IdentifierType.URL](ascredentialserviceidentifier/identifiertype/url.md)
  A URL service identifier.
- [ASCredentialServiceIdentifier.IdentifierType.domain](ascredentialserviceidentifier/identifiertype/domain.md)
  A domain service identifier.
### Enumeration Cases
- [ASCredentialServiceIdentifier.IdentifierType.app](ascredentialserviceidentifier/identifiertype/app.md)
  The service identifier represents an App ID. When a service identifier of this type is provided to your extension for saving a password, the ASCredentialServiceIdentifier object will have a non-nil `displayName` property that contains a user friendly name for the app.
### Initializers
- [init?(rawValue: Int)](ascredentialserviceidentifier/identifiertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var identifier: String](ascredentialserviceidentifier/identifier.md)
  A string that names the identified service.
- [var type: ASCredentialServiceIdentifier.IdentifierType](ascredentialserviceidentifier/type.md)
  The kind of services that the identifier represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier/identifiertype)*