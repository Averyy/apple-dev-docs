# ASWebAuthenticationSessionError

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

Errors that a web authentication session can generate.

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
struct ASWebAuthenticationSessionError
```

## Topics

### Error Domain
- [let ASWebAuthenticationSessionErrorDomain: String](./aswebauthenticationsessionerrordomain.md)
  The error domain for a web authentication session.
- [static var errorDomain: String](./aswebauthenticationsessionerror/errordomain.md)
### Error Codes
- [static var canceledLogin: ASWebAuthenticationSessionError.Code](./aswebauthenticationsessionerror/canceledlogin.md)
  The login has been canceled.
- [static var presentationContextNotProvided: ASWebAuthenticationSessionError.Code](./aswebauthenticationsessionerror/presentationcontextnotprovided.md)
  A context wasn’t provided.
- [static var presentationContextInvalid: ASWebAuthenticationSessionError.Code](./aswebauthenticationsessionerror/presentationcontextinvalid.md)
  The context was invalid.
- [ASWebAuthenticationSessionError.Code](./aswebauthenticationsessionerror/code.md)
  The error code for a web authentication session error.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Recognizing Errors
- [let ASWebAuthenticationSessionErrorDomain: String](./aswebauthenticationsessionerrordomain.md)
  The error domain for a web authentication session.
- [ASWebAuthenticationSessionError.Code](./aswebauthenticationsessionerror/code.md)
  The error code for a web authentication session error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionerror)*