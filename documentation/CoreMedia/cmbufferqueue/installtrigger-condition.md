# installTrigger(condition:_:)

**Framework**: Core Media  
**Kind**: method

Installs a trigger on the queue.

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
func installTrigger(condition: CMBufferQueue.TriggerCondition, _ body: CMBufferQueueTriggerHandler? = nil) throws -> CMBufferQueue.TriggerToken
```

## See Also

- [func removeTrigger(CMBufferQueue.TriggerToken) throws](cmbufferqueue/removetrigger(_:).md)
  Removes a trigger from the queue.
- [func testTrigger(CMBufferQueue.TriggerToken) -> Bool](cmbufferqueue/testtrigger(_:).md)
  Tests a trigger condition.
- [CMBufferQueue.TriggerToken](cmbufferqueue/triggertoken.md)
  A type alias for a trigger token.
- [CMBufferQueue.TriggerCondition](cmbufferqueue/triggercondition.md)
  An enumeration of trigger conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/installtrigger(condition:_:))*