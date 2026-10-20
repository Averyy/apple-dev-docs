# CMBufferQueue.TriggerToken

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

A type alias for a trigger token.

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
typealias TriggerToken = CMBufferQueueTriggerToken
```

## See Also

### Managing Triggers
- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](./installtrigger%28condition,_%29.md)
  Installs a trigger on the queue.
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](./removetrigger%28_%29.md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](./testtrigger%28_%29.md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerCondition](./triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/triggertoken)*