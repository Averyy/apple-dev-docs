# CMBufferQueueInstallTrigger(_:callback:refcon:condition:time:triggerTokenOut:)

**Framework**: Core Media  
**Kind**: func

Installs a trigger with a callback on a buffer queue.

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
func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, time: CMTime, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus
```

#### Return Value

A result code. See `Result Codes`

#### Discussion

The returned trigger token can be passed to `CMBufferQueueTestTrigger` and `CMBufferQueueRemoveTrigger`. The `triggerTokenOut` parameter can be `NULL` (client doesn’t need to test or remove trigger), and the `triggerCallback` parameter can be `NULL` (client doesn’t need callbacks, but rather will explicitly test the trigger).  One of these two parameters must be non-NULL, however, since an untestable trigger that does not perform a callback is meaningless.  If the trigger condition is already true,  `CMBufferQueueInstallTrigger` will call the triggerCallback and will first write the trigger token to *triggerTokenOut.

## Parameters

- `queue`:   on which the trigger is being set.
- `callback`: Callback to be called when the trigger condition becomes true. Can be  , if client intends only to explicitly test the condition.  if   is   this parameter cannot be   otherwise the trigger would be meaningless.
- `refcon`: Refcon to be passed to the triggerCallback. Can be   if the callback doesn’t need it, or is                                                            itself  .
- `condition`: The condition to be tested when evaluating the trigger.
- `time`: The time value to compare against when evaluating the trigger. Must be numeric (ie. not invalid, indefinite, or infinite), except for certain trigger conditions which ignores it (eg, kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges).
- `triggerTokenOut`: Address where created trigger token will be written. Can be  , if client has no need to explicitly test or remove the trigger. Cannot be   when triggerCallback is  ,  since the trigger would be meaningless then.

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
- [func CMBufferQueueTestTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> Bool](cmbufferqueuetesttrigger(_:triggertoken:).md)
  Tests whether the trigger condition is true for the specified buffer queue.
- [func CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, threshold: CMItemCount, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltriggerwithintegerthreshold(_:callback:refcon:condition:threshold:triggertokenout:).md)
  Installs a trigger with a callback and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerCallback](cmbufferqueuetriggercallback.md)
  A callback for the system to invoke when a trigger condition becomes true.
- [typealias CMBufferQueueTriggerCondition](cmbufferqueuetriggercondition.md)
  A type to specify conditions to associate with a buffer queue trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueueinstalltrigger(_:callback:refcon:condition:time:triggertokenout:))*