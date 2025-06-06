# CXErrorCodeIncomingCallError

**Framework**: CallKit  
**Kind**: struct

Codes for errors that occur during incoming calls.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct CXErrorCodeIncomingCallError
```

## Topics

### Errors
- [static var callUUIDAlreadyExists: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/calluuidalreadyexists.md)
  The incoming call UUID already exists.
- [static var filteredByBlockList: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/filteredbyblocklist.md)
  The system is filtering the incoming call because the user is blocking it.
- [static var filteredByDoNotDisturb: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/filteredbydonotdisturb.md)
  The system is filtering the incoming call because Do Not Disturb is active and the incoming caller isn’t a VIP.
- [static var unentitled: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/unentitled.md)
  The app doesn’t have the entitlement to receive incoming calls.
- [static var unknown: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/unknown.md)
  An unknown error occurred.
### Type Properties
- [static var filteredDuringRestrictedSharingMode: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/filteredduringrestrictedsharingmode.md)
- [static var callIsProtected: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/callisprotected.md)
- [static var errorDomain: String](cxerrorcodeincomingcallerror-swift.struct/errordomain.md)
### Enumerations
- [CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CXCallEndedReason](cxcallendedreason.md)
  The reason that a call ended.
- [struct CXError](cxerror.md)
  Error codes for the CallKit errors.
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.
- [CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror-swift.struct)*