# ASWebAuthenticationSessionError.Code

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

The error code for a web authentication session error.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
enum Code
```

```c
enum ASWebAuthenticationSessionErrorCode : NSInteger;
```

## Topics

### Codes
- [ASWebAuthenticationSessionError.Code.canceledLogin](./code/canceledlogin.md)
  The login has been canceled.
- [ASWebAuthenticationSessionError.Code.presentationContextNotProvided](./code/presentationcontextnotprovided.md)
  A context wasn’t provided.
- [ASWebAuthenticationSessionError.Code.presentationContextInvalid](./code/presentationcontextinvalid.md)
  The context was invalid.
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

### Recognizing Errors
- [struct ASWebAuthenticationSessionError](../aswebauthenticationsessionerror.md)
  Errors that a web authentication session can generate.
- [let ASWebAuthenticationSessionErrorDomain: String](../aswebauthenticationsessionerrordomain.md)
  The error domain for a web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionerror/code)*