# CXError.Code

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for the CallKit errors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum CXErrorCode : NSInteger;
```

## Topics

### Constants
- [CXError.Code.invalidArgument](./code/invalidargument.md)
  The argument is invalid.
- [CXError.Code.unentitled](./code/unentitled.md)
  The caller doesn’t have the correct entitlement.
- [CXError.Code.unknownError](./code/unknownerror.md)
  An unknown error occurred.
### Enumeration Cases
- [CXError.Code.missingVoIPBackgroundMode](./code/missingvoipbackgroundmode.md)
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

### Handling Errors
- [enum CXCallEndedReason](../cxcallendedreason.md)
  The reason that a call ended.
- [struct CXError](../cxerror.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](../cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [CXErrorCodeIncomingCallError.Code](../cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](../cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](../cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](../cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerror/code)*