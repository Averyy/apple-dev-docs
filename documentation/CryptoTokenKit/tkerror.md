# TKError

**Framework**: CryptoTokenKit  
**Kind**: struct

An error specific to the CryptoTokenKit framework.

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
struct TKError
```

## Topics

### Checking Error Codes
- [static var notImplemented: TKError.Code](tkerror/notimplemented.md)
  The system doesn’t implement the requested functionality.
- [static var communicationError: TKError.Code](tkerror/communicationerror.md)
  The system had a communication error.
- [static var corruptedData: TKError.Code](tkerror/corrupteddata.md)
  The system idenfitied the data as corrupted.
- [static var canceledByUser: TKError.Code](tkerror/canceledbyuser.md)
  The user canceled the operation.
- [static var authenticationFailed: TKError.Code](tkerror/authenticationfailed.md)
  Authentication failed.
- [static var objectNotFound: TKError.Code](tkerror/objectnotfound.md)
  The system didn’t find the object.
- [static var tokenNotFound: TKError.Code](tkerror/tokennotfound.md)
  The system didn’t find the token.
- [static var badParameter: TKError.Code](tkerror/badparameter.md)
  An invalid parameter was provided.
- [static var authenticationNeeded: TKError.Code](tkerror/authenticationneeded.md)
  Authentication is needed.
- [static var TKErrorAuthenticationFailed: TKError.Code](tkerror/tkerrorauthenticationfailed.md)
- [static var TKErrorObjectNotFound: TKError.Code](tkerror/tkerrorobjectnotfound.md)
- [static var TKErrorTokenNotFound: TKError.Code](tkerror/tkerrortokennotfound.md)
### Type Properties
- [static var errorDomain: String](tkerror/errordomain.md)
- [static var invalidatedDeviceKey: TKError.Code](tkerror/invalidateddevicekey.md)

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let TKErrorDomain: String](tkerrordomain.md)
  The domain for all CryptoTokenKit framework errors.
- [TKError.Code](tkerror/code.md)
  Error codes from CryptoTokenKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkerror)*