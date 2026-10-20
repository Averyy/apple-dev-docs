# removeTrigger(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Removes a trigger from the queue.

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
func removeTrigger(_ triggerToken: CMBufferQueue.TriggerToken) throws
```

## See Also

### Managing Triggers
- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](./installtrigger%28condition,_%29.md)
  Installs a trigger on the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](./testtrigger%28_%29.md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](./triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](./triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/removetrigger(_:))*