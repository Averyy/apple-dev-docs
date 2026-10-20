# SFAuthenticationError

**Framework**: Safari Services  
**Kind**: struct  
**Role**: Structure

An authentication error.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0
- iPadOS 11.0+ - Deprecated in 12.0

> **Deprecated**: Use [`ASWebAuthenticationSessionError`](../AuthenticationServices/aswebauthenticationsessionerror.md) instead.

## Declaration

```swift
struct SFAuthenticationError
```

## Topics

### Type Properties
- [static var canceledLogin: SFAuthenticationError.Code](./sfauthenticationerror-swift.struct/canceledlogin.md)
- [static var errorDomain: String](./sfauthenticationerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [let SFContentBlockerErrorDomain: String](./sfcontentblockererrordomain.md)
  The domain for content blocker errors.
- [enum SFContentBlockerErrorCode](./sfcontentblockererrorcode.md)
  Messages that describe a content blocker error.
- [class SFAuthenticationSession](./sfauthenticationsession.md)
  A class that manages sharing a one-time login between Safari and an app, which can also provide automatic login for associated apps.
- [SFAuthenticationError.Code](./sfauthenticationerror-swift.struct/code.md)
  Messages that describe an authentication error.
- [let SFAuthenticationErrorDomain: String](./sfauthenticationerrordomain.md)
  The domain for authentication errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationerror-swift.struct)*