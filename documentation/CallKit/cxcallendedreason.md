# CXCallEndedReason

**Framework**: CallKit  
**Kind**: enum

The reason that a call ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum CXCallEndedReason
```

#### Overview

Pass these values to the [`reportCall(with:endedAt:reason:)`](cxprovider/reportcall(with:endedat:reason:).md) method.

## Topics

### Constants
- [CXCallEndedReason.failed](cxcallendedreason/failed.md)
  An error occurred while attempting to service the call.
- [CXCallEndedReason.remoteEnded](cxcallendedreason/remoteended.md)
  The remote party explicitly ended the call.
- [CXCallEndedReason.unanswered](cxcallendedreason/unanswered.md)
  The call never started connecting and was never explicitly ended, such as when an outgoing or incoming call times out.
- [CXCallEndedReason.answeredElsewhere](cxcallendedreason/answeredelsewhere.md)
  Another device answered the call.
- [CXCallEndedReason.declinedElsewhere](cxcallendedreason/declinedelsewhere.md)
  Another device declined the call.
### Initializers
- [init?(rawValue: Int)](cxcallendedreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CXError](cxerror.md)
  Error codes for the CallKit errors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallendedreason)*