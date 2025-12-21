# CMBufferQueueTestTrigger(_:triggerToken:)

**Framework**: Core Media  
**Kind**: func

Tests whether the trigger condition is true for the specified buffer queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueTestTrigger(_ queue: CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> Bool
```

#### Return Value

A Boolean indicating whether the trigger condition is True.

#### Discussion

[`CMBufferQueue`](cmbufferqueue-api.md) always returns the condition’s current status. The trigger callback will only be called when the condition goes from false to true. The `triggerToken` must be one that has been installed on this queue.

## Parameters

- `queue`:   on which the trigger is tested.
- `triggerToken`: Trigger to test.

## See Also

- [func CMBufferQueueInstallTriggerHandler(CMBufferQueue, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandler(_:_:_:_:_:).md)
  Installs a trigger with a handler on a buffer queue.
- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandlerwithintegerthreshold(_:_:_:_:_:).md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [typealias CMBufferQueueTriggerToken](cmbufferqueuetriggertoken.md)
  A type alias for a trigger token.
- [Buffer Trigger Conditions](buffer-trigger-conditions.md)
  The trigger conditions the framework supports.
- [func CMBufferQueueInstallTrigger(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, time: CMTime, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltrigger(_:callback:refcon:condition:time:triggertokenout:).md)
  Installs a trigger with a callback on a buffer queue.
- [func CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, threshold: CMItemCount, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltriggerwithintegerthreshold(_:callback:refcon:condition:threshold:triggertokenout:).md)
  Installs a trigger with a callback and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerCallback](cmbufferqueuetriggercallback.md)
  A callback for the system to invoke when a trigger condition becomes true.
- [typealias CMBufferQueueTriggerCondition](cmbufferqueuetriggercondition.md)
  A type to specify conditions to associate with a buffer queue trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuetesttrigger(_:triggertoken:))*