# kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan

**Framework**: Core Media  
**Kind**: var

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan: CMBufferQueueTriggerCondition { get }
```

## See Also

- [var kCMBufferQueueTrigger_WhenDurationBecomesLessThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomeslessthan.md)
  Trigger fires when queue duration becomes less than the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomeslessthanorequalto.md)
  Trigger fires when queue duration becomes less than or equal to the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomesgreaterthan.md)
  Trigger fires when queue duration becomes greater than the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequalto.md)
  Trigger fires when queue duration becomes greater than or equal to the specified duration.
- [var kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenminpresentationtimestampchanges.md)
  Trigger fires when the minimum presentation timestamp changes (triggerDuration is ignored).
- [var kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenmaxpresentationtimestampchanges.md)
  Trigger fires when the maximum presentation timestamp changes (triggerDuration is ignored).
- [var kCMBufferQueueTrigger_WhenDataBecomesReady: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendatabecomesready.md)
  Trigger fires when next dequeueable buffer becomes ready (that is, [`CMBufferQueueDequeueIfDataReady(_:)`](cmbufferqueuedequeueifdataready(_:).md) will now succeed).  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenEndOfDataReached: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenendofdatareached.md)
  Trigger fires when CMBufferQueueIsAtEndOfData’s condition becomes true.  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenReset: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenreset.md)
  Trigger fires when CMBufferQueueReset called.  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenbuffercountbecomeslessthan.md)
  Trigger fires when buffer count becomes less than the specified threshold number.
- [var kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenbuffercountbecomesgreaterthan.md)
  Trigger fires when buffer count becomes > the specified threshold number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequaltoandbuffercountbecomesgreaterthan)*