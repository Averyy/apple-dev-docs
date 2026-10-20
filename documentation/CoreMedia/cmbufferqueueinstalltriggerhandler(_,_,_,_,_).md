# CMBufferQueueInstallTriggerHandler(_:_:_:_:_:)

**Framework**: Core Media  
**Kind**: func

Installs a trigger with a handler on a buffer queue.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueInstallTriggerHandler(_ queue: CMBufferQueue, _ condition: CMBufferQueueTriggerCondition, _ time: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, _ handler: CMBufferQueueTriggerHandler?) -> OSStatus
```

## See Also

- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandlerwithintegerthreshold(_:_:_:_:_:).md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [typealias CMBufferQueueTriggerToken](cmbufferqueuetriggertoken.md)
  A type alias for a trigger token.
- [Buffer Trigger Conditions](buffer-trigger-conditions.md)
  The trigger conditions the framework supports.
- [func CMBufferQueueTestTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> Bool](cmbufferqueuetesttrigger(_:triggertoken:).md)
  Tests whether the trigger condition is true for the specified buffer queue.
- [func CMBufferQueueInstallTrigger(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, time: CMTime, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltrigger(_:callback:refcon:condition:time:triggertokenout:).md)
  Installs a trigger with a callback on a buffer queue.
- [func CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, threshold: CMItemCount, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltriggerwithintegerthreshold(_:callback:refcon:condition:threshold:triggertokenout:).md)
  Installs a trigger with a callback and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerCallback](cmbufferqueuetriggercallback.md)
  A callback for the system to invoke when a trigger condition becomes true.
- [typealias CMBufferQueueTriggerCondition](cmbufferqueuetriggercondition.md)
  A type to specify conditions to associate with a buffer queue trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueueinstalltriggerhandler(_:_:_:_:_:))*