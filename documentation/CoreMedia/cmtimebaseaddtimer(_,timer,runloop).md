# CMTimebaseAddTimer(_:timer:runloop:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CMTimebaseAddTimer(CMTimebaseRef timebase, CFRunLoopTimerRef timer, CFRunLoopRef runloop);
```

## Discussion

The timer must be a repeating runloop timer (with a very long interval at least as long as the constant [`kCMTimebaseVeryLongCFTimeInterval`](./kcmtimebaseverylongcftimeinterval.md)) attached to a runloop. The timebase retains the timer, and maintains its “NextFireDate” according to the `CMTime` set using [`CMTimebaseSetTimerNextFireTime(_:timer:fireTime:flags:)`](./cmtimebasesettimernextfiretime%28_,timer,firetime,flags%29.md). Until the first call to `CMTimebaseSetTimerNextFireTime`, the system sets the “NextFireDate” to a future time. The function retains the  runloop you specify, which must be the runloop you attached to the timer when you created it. The system uses the retained runloop to call `CFRunLoopWakeUp`() when the timebase modifies the timer’s fire date.

## See Also

### Interacting with Timers
- [func CMTimebaseAddTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebaseaddtimerdispatchsource%28_,timersource%29.md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func CMTimebaseRemoveTimer(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebaseremovetimer%28_,timer%29.md)
  Removes the timer from the list of timers the timebase manages.
- [func CMTimebaseRemoveTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebaseremovetimerdispatchsource%28_,timersource%29.md)
  Removes the timer dispatch source from the list of timers the timebase manages.
- [func CMTimebaseSetTimerNextFireTime(CMTimebase, timer: CFRunLoopTimer, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimernextfiretime%28_,timer,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func CMTimebaseSetTimerToFireImmediately(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebasesettimertofireimmediately%28_,timer%29.md)
  Sets the timer to fire immediately once, overriding any previous timer calls.
- [func CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase, timerSource: dispatch_source_t, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimerdispatchsourcenextfiretime%28_,timersource,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebasesettimerdispatchsourcetofireimmediately%28_,timersource%29.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous timer call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseaddtimer(_:timer:runloop:))*