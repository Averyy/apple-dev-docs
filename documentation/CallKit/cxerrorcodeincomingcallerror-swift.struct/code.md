# CXErrorCodeIncomingCallError.Code

**Framework**: CallKit  
**Kind**: enum

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

## Topics

### Errors
- [CXErrorCodeIncomingCallError.Code.unknown](cxerrorcodeincomingcallerror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeIncomingCallError.Code.unentitled](cxerrorcodeincomingcallerror-swift.struct/code/unentitled.md)
  The app isn’t entitled to receive incoming calls.
- [CXErrorCodeIncomingCallError.Code.callUUIDAlreadyExists](cxerrorcodeincomingcallerror-swift.struct/code/calluuidalreadyexists.md)
  The incoming call UUID already exists.
- [CXErrorCodeIncomingCallError.Code.filteredByDoNotDisturb](cxerrorcodeincomingcallerror-swift.struct/code/filteredbydonotdisturb.md)
  The incoming call is filtered because Do Not Disturb is active and the incoming caller is not a VIP.
- [CXErrorCodeIncomingCallError.Code.filteredByBlockList](cxerrorcodeincomingcallerror-swift.struct/code/filteredbyblocklist.md)
  The incoming call is filtered because the incoming caller has been blocked by the user.
### Enumeration Cases
- [CXErrorCodeIncomingCallError.Code.filteredDuringRestrictedSharingMode](cxerrorcodeincomingcallerror-swift.struct/code/filteredduringrestrictedsharingmode.md)
- [CXErrorCodeIncomingCallError.Code.callIsProtected](cxerrorcodeincomingcallerror-swift.struct/code/callisprotected.md)
### Initializers
- [init?(rawValue: Int)](cxerrorcodeincomingcallerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CXCallEndedReason](cxcallendedreason.md)
  The reason that a call ended.
- [struct CXError](cxerror.md)
  Error codes for the CallKit errors.
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror-swift.struct/code)*