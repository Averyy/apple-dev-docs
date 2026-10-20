# installTrigger(condition:_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Installs a trigger on the queue.

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
func installTrigger(condition: CMBufferQueue.TriggerCondition, _ body: CMBufferQueueTriggerHandler? = nil) throws -> CMBufferQueue.TriggerToken
```

## See Also

### Managing Triggers
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](./removetrigger%28_%29.md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](./testtrigger%28_%29.md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](./triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](./triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/installtrigger(condition:_:))*