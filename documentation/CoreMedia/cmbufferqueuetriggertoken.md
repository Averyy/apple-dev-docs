# CMBufferQueueTriggerToken

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

A type alias for a trigger token.

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
typealias CMBufferQueueTriggerToken = OpaquePointer
```

```c
typedef struct opaqueCMBufferQueueTriggerToken * CMBufferQueueTriggerToken;
```

#### Discussion

The CMBufferQueueTriggerToken is returned from [`CMBufferQueueInstallTrigger(_:callback:refcon:condition:time:triggerTokenOut:)`](./cmbufferqueueinstalltrigger%28_,callback,refcon,condition,time,triggertokenout%29.md), so you can remove it later if necessary.  Triggers will automatically be removed when the queue is finalized. Note that if more than one module has access to a queue, it may be hard for an individual module to know when the queue is finalized since other modules may retain it.  To address this concern, modules should remove their triggers before they themselves are finalized.

##### Special Considerations

A `CMBufferQueueTrigger` is not a Core Foundation object; you must not `CFRetain` or `CFRelease` it.

## See Also

### Managing Triggers
- [func CMBufferQueueInstallTriggerHandler(CMBufferQueue, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](./cmbufferqueueinstalltriggerhandler%28_,_,_,_,_%29.md)
  Installs a trigger with a handler on a buffer queue.
- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](./cmbufferqueueinstalltriggerhandlerwithintegerthreshold%28_,_,_,_,_%29.md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](./cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [Buffer Trigger Conditions](./buffer-trigger-conditions.md)
  The trigger conditions the framework supports.
- [func CMBufferQueueTestTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> Bool](./cmbufferqueuetesttrigger%28_,triggertoken%29.md)
  Tests whether the trigger condition is true for the specified buffer queue.
- [func CMBufferQueueInstallTrigger(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, time: CMTime, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](./cmbufferqueueinstalltrigger%28_,callback,refcon,condition,time,triggertokenout%29.md)
  Installs a trigger with a callback on a buffer queue.
- [func CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, threshold: CMItemCount, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](./cmbufferqueueinstalltriggerwithintegerthreshold%28_,callback,refcon,condition,threshold,triggertokenout%29.md)
  Installs a trigger with a callback and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerCallback](./cmbufferqueuetriggercallback.md)
  A callback for the system to invoke when a trigger condition becomes true.
- [typealias CMBufferQueueTriggerCondition](./cmbufferqueuetriggercondition.md)
  A type to specify conditions to associate with a buffer queue trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuetriggertoken)*