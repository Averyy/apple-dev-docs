# CMBufferQueueTriggerCondition

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

A type to specify conditions to associate with a buffer queue trigger.

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
typealias CMBufferQueueTriggerCondition = Int32
```

```c
typedef int32_t CMBufferQueueTriggerCondition;
```

#### Discussion

For possible values, see [Buffer Trigger Conditions](./buffer-trigger-conditions.md).

## See Also

### Managing Triggers
- [func CMBufferQueueInstallTriggerHandler(CMBufferQueue, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](./cmbufferqueueinstalltriggerhandler%28_,_,_,_,_%29.md)
  Installs a trigger with a handler on a buffer queue.
- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](./cmbufferqueueinstalltriggerhandlerwithintegerthreshold%28_,_,_,_,_%29.md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](./cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [typealias CMBufferQueueTriggerToken](./cmbufferqueuetriggertoken.md)
  A type alias for a trigger token.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuetriggercondition)*