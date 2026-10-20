# TKError.Code

**Framework**: CryptoTokenKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum TKErrorCode : NSInteger;
```

## Topics

### Error Codes
- [TKError.Code.notImplemented](./code/notimplemented.md)
  The functionality is not implemented.
- [TKError.Code.communicationError](./code/communicationerror.md)
  A communication error occurred.
- [TKError.Code.corruptedData](./code/corrupteddata.md)
  The data was corrupted.
- [TKError.Code.canceledByUser](./code/canceledbyuser.md)
  The operation was canceled by the user.
- [TKError.Code.authenticationFailed](./code/authenticationfailed.md)
  Authentication failed.
- [TKError.Code.objectNotFound](./code/objectnotfound.md)
  The object was not found.
- [TKError.Code.tokenNotFound](./code/tokennotfound.md)
  The token was not found.
- [TKError.Code.badParameter](./code/badparameter.md)
  An invalid parameter was provided.
- [TKError.Code.authenticationNeeded](./code/authenticationneeded.md)
  Authentication is needed.
- [static var TKErrorAuthenticationFailed: TKError.Code](./code/tkerrorauthenticationfailed.md)
- [static var TKErrorObjectNotFound: TKError.Code](./code/tkerrorobjectnotfound.md)
- [static var TKErrorTokenNotFound: TKError.Code](./code/tkerrortokennotfound.md)
### Enumeration Cases
- [TKError.Code.invalidatedDeviceKey](./code/invalidateddevicekey.md)
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

### Errors
- [struct TKError](../tkerror.md)
  An error specific to the CryptoTokenKit framework.
- [let TKErrorDomain: String](../tkerrordomain.md)
  The domain for all CryptoTokenKit framework errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code)*