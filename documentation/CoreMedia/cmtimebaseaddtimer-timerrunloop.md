# CMTimebaseAddTimer(_:timer:runloop:)

**Framework**: Core Media  
**Kind**: func

Adds the timer to the list of timers the timebase manages.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimebaseAddTimer(_ timebase: CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus
```

#### Discussion

The timer must be a repeating runloop timer (with a very long interval at least as long as the constant [`kCMTimebaseVeryLongCFTimeInterval`](kcmtimebaseverylongcftimeinterval.md)) attached to a runloop. The timebase retains the timer, and maintains its “NextFireDate” according to the `CMTime` set using [`CMTimebaseSetTimerNextFireTime(_:timer:fireTime:flags:)`](cmtimebasesettimernextfiretime(_:timer:firetime:flags:).md). Until the first call to `CMTimebaseSetTimerNextFireTime`, the system sets the “NextFireDate” to a future time. The function retains the  runloop you specify, which must be the runloop you attached to the timer when you created it. The system uses the retained runloop to call `CFRunLoopWakeUp`() when the timebase modifies the timer’s fire date.

## See Also

- [func CMTimebaseAddTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](cmtimebaseaddtimerdispatchsource(_:timersource:).md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func CMTimebaseRemoveTimer(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](cmtimebaseremovetimer(_:timer:).md)
  Removes the timer from the list of timers the timebase manages.
- [func CMTimebaseRemoveTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](cmtimebaseremovetimerdispatchsource(_:timersource:).md)
  Removes the timer dispatch source from the list of timers the timebase manages.
- [func CMTimebaseSetTimerNextFireTime(CMTimebase, timer: CFRunLoopTimer, fireTime: CMTime, flags: UInt32) -> OSStatus](cmtimebasesettimernextfiretime(_:timer:firetime:flags:).md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func CMTimebaseSetTimerToFireImmediately(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](cmtimebasesettimertofireimmediately(_:timer:).md)
  Sets the timer to fire immediately once, overriding any previous timer calls.
- [func CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase, timerSource: dispatch_source_t, fireTime: CMTime, flags: UInt32) -> OSStatus](cmtimebasesettimerdispatchsourcenextfiretime(_:timersource:firetime:flags:).md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](cmtimebasesettimerdispatchsourcetofireimmediately(_:timersource:).md)
  Sets the timer dispatch source to fire immediately once, overriding any previous timer call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseaddtimer(_:timer:runloop:))*