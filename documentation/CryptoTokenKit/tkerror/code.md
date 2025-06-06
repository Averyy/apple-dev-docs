# TKError.Code

**Framework**: CryptoTokenKit  
**Kind**: enum

Error codes from CryptoTokenKit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [TKError.Code.notImplemented](tkerror/code/notimplemented.md)
  The functionality is not implemented.
- [TKError.Code.communicationError](tkerror/code/communicationerror.md)
  A communication error occurred.
- [TKError.Code.corruptedData](tkerror/code/corrupteddata.md)
  The data was corrupted.
- [TKError.Code.canceledByUser](tkerror/code/canceledbyuser.md)
  The operation was canceled by the user.
- [TKError.Code.authenticationFailed](tkerror/code/authenticationfailed.md)
  Authentication failed.
- [TKError.Code.objectNotFound](tkerror/code/objectnotfound.md)
  The object was not found.
- [TKError.Code.tokenNotFound](tkerror/code/tokennotfound.md)
  The token was not found.
- [TKError.Code.badParameter](tkerror/code/badparameter.md)
  An invalid parameter was provided.
- [TKError.Code.authenticationNeeded](tkerror/code/authenticationneeded.md)
  Authentication is needed.
- [static var TKErrorAuthenticationFailed: TKError.Code](tkerror/code/tkerrorauthenticationfailed.md)
- [static var TKErrorObjectNotFound: TKError.Code](tkerror/code/tkerrorobjectnotfound.md)
- [static var TKErrorTokenNotFound: TKError.Code](tkerror/code/tkerrortokennotfound.md)
### Initializers
- [init?(rawValue: Int)](tkerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct TKError](tkerror.md)
  An error specific to the CryptoTokenKit framework.
- [let TKErrorDomain: String](tkerrordomain.md)
  The domain for all CryptoTokenKit framework errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code)*