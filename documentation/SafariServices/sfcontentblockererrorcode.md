# SFContentBlockerErrorCode

**Framework**: Safari Services  
**Kind**: enum  
**Role**: Enumeration

Messages that describe a content blocker error.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0 (renamed: SFErrorCode)
- iPadOS 9.0+ - Deprecated in 10.0 (renamed: SFErrorCode)
- Mac Catalyst 13.4+ - Deprecated in 13.4 (renamed: SFErrorCode)

> **Deprecated**: Use [`SFError.Code`](./sferror/code.md) instead.

## Declaration

```swift
enum SFContentBlockerErrorCode
```

```c
enum SFContentBlockerErrorCode : NSInteger;
```

## Topics

### Constants
- [SFContentBlockerErrorCode.noExtensionFound](./sfcontentblockererrorcode/noextensionfound.md)
- [SFContentBlockerErrorCode.noAttachmentFound](./sfcontentblockererrorcode/noattachmentfound.md)
- [SFContentBlockerErrorCode.loadingInterrupted](./sfcontentblockererrorcode/loadinginterrupted.md)
### Initializers
- [init?(rawValue: Int)](./sfcontentblockererrorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [let SFContentBlockerErrorDomain: String](./sfcontentblockererrordomain.md)
  The domain for content blocker errors.
- [class SFAuthenticationSession](./sfauthenticationsession.md)
  A class that manages sharing a one-time login between Safari and an app, which can also provide automatic login for associated apps.
- [struct SFAuthenticationError](./sfauthenticationerror-swift.struct.md)
  An authentication error.
- [SFAuthenticationError.Code](./sfauthenticationerror-swift.struct/code.md)
  Messages that describe an authentication error.
- [let SFAuthenticationErrorDomain: String](./sfauthenticationerrordomain.md)
  The domain for authentication errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode)*