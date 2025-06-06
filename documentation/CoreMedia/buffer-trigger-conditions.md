# Buffer Trigger Conditions

**Framework**: Core Media

The trigger conditions the framework supports.

## Topics

### Constants
- [var kCMBufferQueueTrigger_WhenDurationBecomesLessThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomeslessthan.md)
  Trigger fires when queue duration becomes less than the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomeslessthanorequalto.md)
  Trigger fires when queue duration becomes less than or equal to the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomesgreaterthan.md)
  Trigger fires when queue duration becomes greater than the specified duration.
- [var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequalto.md)
  Trigger fires when queue duration becomes greater than or equal to the specified duration.
- [var kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenminpresentationtimestampchanges.md)
  Trigger fires when the minimum presentation timestamp changes (triggerDuration is ignored).
- [var kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenmaxpresentationtimestampchanges.md)
  Trigger fires when the maximum presentation timestamp changes (triggerDuration is ignored).
- [var kCMBufferQueueTrigger_WhenDataBecomesReady: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendatabecomesready.md)
  Trigger fires when next dequeueable buffer becomes ready (that is, [`CMBufferQueueDequeueIfDataReady(_:)`](cmbufferqueuedequeueifdataready(_:).md) will now succeed).  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenEndOfDataReached: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenendofdatareached.md)
  Trigger fires when CMBufferQueueIsAtEndOfData’s condition becomes true.  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenReset: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenreset.md)
  Trigger fires when CMBufferQueueReset called.  (triggerDuration is ignored.)
- [var kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenbuffercountbecomeslessthan.md)
  Trigger fires when buffer count becomes less than the specified threshold number.
- [var kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whenbuffercountbecomesgreaterthan.md)
  Trigger fires when buffer count becomes > the specified threshold number.
- [var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan: CMBufferQueueTriggerCondition](kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequaltoandbuffercountbecomesgreaterthan.md)

## See Also

- [func CMBufferQueueInstallTriggerHandler(CMBufferQueue, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandler(_:_:_:_:_:).md)
  Installs a trigger with a handler on a buffer queue.
- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandlerwithintegerthreshold(_:_:_:_:_:).md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [typealias CMBufferQueueTriggerToken](cmbufferqueuetriggertoken.md)
  A type alias for a trigger token.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/buffer-trigger-conditions)*