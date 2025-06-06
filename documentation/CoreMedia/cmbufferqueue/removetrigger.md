# removeTrigger(_:)

**Framework**: Core Media  
**Kind**: method

Removes a trigger from the queue.

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
func removeTrigger(_ triggerToken: CMBufferQueue.TriggerToken) throws
```

## See Also

- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](cmbufferqueue/installtrigger(condition:_:).md)
  Installs a trigger on the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](cmbufferqueue/testtrigger(_:).md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](cmbufferqueue/triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](cmbufferqueue/triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/removetrigger(_:))*