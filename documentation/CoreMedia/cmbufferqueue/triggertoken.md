# CMBufferQueue.TriggerToken

**Framework**: Core Media  
**Kind**: typealias

A type alias for a trigger token.

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
typealias TriggerToken = CMBufferQueueTriggerToken
```

## See Also

- [func installTrigger(condition: CMBufferQueue.TriggerCondition, CMBufferQueueTriggerHandler?) throws -> CMBufferQueue.TriggerToken](cmbufferqueue/installtrigger(condition:_:).md)
  Installs a trigger on the queue.
- [func removeTrigger(CMBufferQueue.TriggerToken) throws](cmbufferqueue/removetrigger(_:).md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](cmbufferqueue/testtrigger(_:).md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerCondition](cmbufferqueue/triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/triggertoken)*