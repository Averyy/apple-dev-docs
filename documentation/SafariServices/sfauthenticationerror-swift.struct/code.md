# SFAuthenticationError.Code

**Framework**: Safari Services  
**Kind**: enum  
**Role**: Enumeration

Messages that describe an authentication error.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0
- iPadOS 11.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`ASWebAuthenticationSessionError.Code`](../../AuthenticationServices/aswebauthenticationsessionerror/code.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
enum Code
```

*Mac Catalyst*

```swift
enum SFAuthenticationError
```

```c
enum SFAuthenticationError : NSInteger;
```

## Topics

### Enumeration Cases
- [SFAuthenticationError.Code.canceledLogin](./code/canceledlogin.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [let SFContentBlockerErrorDomain: String](../sfcontentblockererrordomain.md)
  The domain for content blocker errors.
- [enum SFContentBlockerErrorCode](../sfcontentblockererrorcode.md)
  Messages that describe a content blocker error.
- [class SFAuthenticationSession](../sfauthenticationsession.md)
  A class that manages sharing a one-time login between Safari and an app, which can also provide automatic login for associated apps.
- [struct SFAuthenticationError](../sfauthenticationerror-swift.struct.md)
  An authentication error.
- [let SFAuthenticationErrorDomain: String](../sfauthenticationerrordomain.md)
  The domain for authentication errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationerror-swift.struct/code)*