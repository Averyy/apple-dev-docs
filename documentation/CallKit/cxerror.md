# CXError

**Framework**: CallKit  
**Kind**: struct

Error codes for the CallKit errors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct CXError
```

## Topics

### Constants
- [static var invalidArgument: CXError.Code](cxerror/invalidargument.md)
  The argument is invalid.
- [static var unentitled: CXError.Code](cxerror/unentitled.md)
  The caller doesn’t have the correct entitlement.
- [static var unknownError: CXError.Code](cxerror/unknownerror.md)
  An unknown error occurred.
### Type Properties
- [static var missingVoIPBackgroundMode: CXError.Code](cxerror/missingvoipbackgroundmode.md)
- [static var errorDomain: String](cxerror/errordomain.md)
### Enumerations
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.

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
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerror)*