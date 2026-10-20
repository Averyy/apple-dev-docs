# CXErrorCodeIncomingCallError.Code

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

Codes for errors that occur during incoming calls.

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
enum CXErrorCodeIncomingCallError : NSInteger;
```

## Topics

### Errors
- [CXErrorCodeIncomingCallError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeIncomingCallError.Code.unentitled](./code/unentitled.md)
  The app isn’t entitled to receive incoming calls.
- [CXErrorCodeIncomingCallError.Code.callUUIDAlreadyExists](./code/calluuidalreadyexists.md)
  The incoming call UUID already exists.
- [CXErrorCodeIncomingCallError.Code.filteredByDoNotDisturb](./code/filteredbydonotdisturb.md)
  The incoming call is filtered because Do Not Disturb is active and the incoming caller is not a VIP.
- [CXErrorCodeIncomingCallError.Code.filteredByBlockList](./code/filteredbyblocklist.md)
  The incoming call is filtered because the incoming caller has been blocked by the user.
### Enumeration Cases
- [CXErrorCodeIncomingCallError.Code.filteredDuringRestrictedSharingMode](./code/filteredduringrestrictedsharingmode.md)
- [CXErrorCodeIncomingCallError.Code.callIsProtected](./code/callisprotected.md)
- [CXErrorCodeIncomingCallError.Code.filteredBySensitiveParticipants](./code/filteredbysensitiveparticipants.md)
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
- [CXError.Code](../cxerror/code.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](../cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](../cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](../cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](../cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror-swift.struct/code)*