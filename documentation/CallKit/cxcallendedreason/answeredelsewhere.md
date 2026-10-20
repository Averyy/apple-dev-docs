# CXCallEndedReason.answeredElsewhere

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

Another device answered the call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case answeredElsewhere
```

```c
CXCallEndedReasonAnsweredElsewhere
```

## See Also

### Constants
- [CXCallEndedReason.failed](./failed.md)
  An error occurred while attempting to service the call.
- [CXCallEndedReason.remoteEnded](./remoteended.md)
  The remote party explicitly ended the call.
- [CXCallEndedReason.unanswered](./unanswered.md)
  The call never started connecting and was never explicitly ended, such as when an outgoing or incoming call times out.
- [CXCallEndedReason.declinedElsewhere](./declinedelsewhere.md)
  Another device declined the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallendedreason/answeredelsewhere)*