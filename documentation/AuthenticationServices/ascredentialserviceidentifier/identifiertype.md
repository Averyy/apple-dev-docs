# ASCredentialServiceIdentifier.IdentifierType

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ASCredentialServiceIdentifierType : NSInteger;
```

## Topics

### Identifier types
- [ASCredentialServiceIdentifier.IdentifierType.URL](./identifiertype/url.md)
  A URL service identifier.
- [ASCredentialServiceIdentifier.IdentifierType.domain](./identifiertype/domain.md)
  A domain service identifier.
### Enumeration Cases
- [ASCredentialServiceIdentifier.IdentifierType.app](./identifiertype/app.md)
  The service identifier represents an App ID. When a service identifier of this type is provided to your extension for saving a password, the ASCredentialServiceIdentifier object will have a non-nil `displayName` property that contains a user friendly name for the app.
### Initializers
- [init?(rawValue: Int)](./identifiertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the credential service
- [var identifier: String](./identifier.md)
  A string that names the identified service.
- [var type: ASCredentialServiceIdentifier.IdentifierType](./type.md)
  The kind of services that the identifier represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier/identifiertype)*