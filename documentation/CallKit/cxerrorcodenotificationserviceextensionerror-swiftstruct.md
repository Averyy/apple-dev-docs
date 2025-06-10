# CXErrorCodeNotificationServiceExtensionError

**Framework**: CallKit  
**Kind**: struct

Errors that can occur when reporting new, incoming VoIP calls.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct CXErrorCodeNotificationServiceExtensionError
```

#### Overview

The system can return these errors to the [`reportNewIncomingVoIPPushPayload(_:completion:)`](cxprovider/reportnewincomingvoippushpayload(_:completion:).md) method’s completion handler.

## Topics

### Understanding Error Codes
- [static var invalidClientProcess: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/invalidclientprocess.md)
  An error indicating that an invalid client process reported the incoming call.
- [static var missingNotificationFilteringEntitlement: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [static var unknown: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/unknown.md)
  An error that occurs when there is an unknown problem.
- [CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/code.md)
  Constants for errors returned when reporting new, incoming VoIP calls.
### Type Properties
- [static var errorDomain: String](cxerrorcodenotificationserviceextensionerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CXCallEndedReason](cxcallendedreason.md)
  The reason that a call ended.
- [struct CXError](cxerror.md)
  Error codes for the CallKit errors.
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.
- [let CXErrorDomain: String](cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct)*