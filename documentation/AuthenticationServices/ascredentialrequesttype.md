# ASCredentialRequestType

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

An enumeration that identifies different types of credentials that apps and websites can request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum ASCredentialRequestType
```

```c
enum ASCredentialRequestType : NSInteger;
```

## Topics

### Credential types
- [ASCredentialRequestType.passkeyAssertion](./ascredentialrequesttype/passkeyassertion.md)
  The app or website is requesting a passkey assertion credential.
- [ASCredentialRequestType.passkeyRegistration](./ascredentialrequesttype/passkeyregistration.md)
  The app or website is requesting a passkey registration credential.
- [ASCredentialRequestType.password](./ascredentialrequesttype/password.md)
  The app or website is requesting a password credential.
- [ASCredentialRequestType.oneTimeCode](./ascredentialrequesttype/onetimecode.md)
  The app or website is requesting a one-time passcode.
### Initializers
- [init?(rawValue: Int)](./ascredentialrequesttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying the requested credential type
- [var type: ASCredentialRequestType](./ascredentialrequest/type.md)
  The type of credential used for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialrequesttype)*