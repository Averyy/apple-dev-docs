# CXCallEndedReason.unanswered

**Framework**: CallKit  
**Kind**: case

The call never started connecting and was never explicitly ended, such as when an outgoing or incoming call times out.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case unanswered
```

## See Also

- [CXCallEndedReason.failed](cxcallendedreason/failed.md)
  An error occurred while attempting to service the call.
- [CXCallEndedReason.remoteEnded](cxcallendedreason/remoteended.md)
  The remote party explicitly ended the call.
- [CXCallEndedReason.answeredElsewhere](cxcallendedreason/answeredelsewhere.md)
  Another device answered the call.
- [CXCallEndedReason.declinedElsewhere](cxcallendedreason/declinedelsewhere.md)
  Another device declined the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallendedreason/unanswered)*