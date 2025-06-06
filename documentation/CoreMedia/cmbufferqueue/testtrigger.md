# testTrigger(_:)

**Framework**: Core Media  
**Kind**: method

Tests a trigger condition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func testTrigger(_ triggerToken: CMBufferQueue.TriggerToken) -> Bool
```

## See Also

- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](cmbufferqueue/installtrigger(condition:_:).md)
  Installs a trigger on the queue.
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](cmbufferqueue/removetrigger(_:).md)
  Removes a trigger from the queue.
- [CMBufferQueue.TriggerToken](cmbufferqueue/triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](cmbufferqueue/triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/testtrigger(_:))*