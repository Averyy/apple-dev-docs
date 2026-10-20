# SFAuthenticationErrorDomain

**Framework**: Safari Services  
**Kind**: var  
**Role**: Global Variable

The domain for authentication errors.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSessionErrorDomain)
- iPadOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSessionErrorDomain)
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`ASWebAuthenticationSessionErrorDomain`](../AuthenticationServices/aswebauthenticationsessionerrordomain.md) instead.

## Declaration

```swift
let SFAuthenticationErrorDomain: String
```

```c
extern NSString * const SFAuthenticationErrorDomain;
```

## See Also

### Deprecated
- [let SFContentBlockerErrorDomain: String](./sfcontentblockererrordomain.md)
  The domain for content blocker errors.
- [enum SFContentBlockerErrorCode](./sfcontentblockererrorcode.md)
  Messages that describe a content blocker error.
- [class SFAuthenticationSession](./sfauthenticationsession.md)
  A class that manages sharing a one-time login between Safari and an app, which can also provide automatic login for associated apps.
- [struct SFAuthenticationError](./sfauthenticationerror-swift.struct.md)
  An authentication error.
- [SFAuthenticationError.Code](./sfauthenticationerror-swift.struct/code.md)
  Messages that describe an authentication error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationerrordomain)*