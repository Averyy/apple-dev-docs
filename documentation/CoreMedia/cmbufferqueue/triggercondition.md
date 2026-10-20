# CMBufferQueue.TriggerCondition

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

An enumeration of trigger conditions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum TriggerCondition
```

## Topics

### Conditions
- [CMBufferQueue.TriggerCondition.whenBufferCountBecomesGreaterThan(_:)](./triggercondition/whenbuffercountbecomesgreaterthan%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenBufferCountBecomesLessThan(_:)](./triggercondition/whenbuffercountbecomeslessthan%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenDataBecomesReady](./triggercondition/whendatabecomesready.md)
- [CMBufferQueue.TriggerCondition.whenDurationBecomesGreaterThan(_:)](./triggercondition/whendurationbecomesgreaterthan%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenDurationBecomesGreaterThanOrEqualTo(_:)](./triggercondition/whendurationbecomesgreaterthanorequalto%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenDurationBecomesLessThan(_:)](./triggercondition/whendurationbecomeslessthan%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenDurationBecomesLessThanOrEqualTo(_:)](./triggercondition/whendurationbecomeslessthanorequalto%28_%29.md)
- [CMBufferQueue.TriggerCondition.whenEndOfDataReached](./triggercondition/whenendofdatareached.md)
- [CMBufferQueue.TriggerCondition.whenMaxPresentationTimeStampChanges](./triggercondition/whenmaxpresentationtimestampchanges.md)
- [CMBufferQueue.TriggerCondition.whenMinPresentationTimeStampChanges](./triggercondition/whenminpresentationtimestampchanges.md)
- [CMBufferQueue.TriggerCondition.whenReset](./triggercondition/whenreset.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Triggers
- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](./installtrigger%28condition,_%29.md)
  Installs a trigger on the queue.
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](./removetrigger%28_%29.md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](./testtrigger%28_%29.md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](./triggertoken.md)
  A type alias for a trigger token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/triggercondition)*