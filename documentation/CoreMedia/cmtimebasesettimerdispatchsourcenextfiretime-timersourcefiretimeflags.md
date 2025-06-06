# CMTimebaseSetTimerDispatchSourceNextFireTime(_:timerSource:fireTime:flags:)

**Framework**: Core Media  
**Kind**: func

Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.

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
func CMTimebaseSetTimerDispatchSourceNextFireTime(_ timebase: CMTimebase, timerSource: dispatch_source_t, fireTime: CMTime, flags: UInt32) -> OSStatus
```

#### Discussion

The timer source you specify must be on the list of timers the timebase manages. The timebase continues to update the timer dispatch source’s start time according to time jumps and effective rate changes. If `fireTime` is not numeric, or if the timebase is not moving, the function sets start time to `DISPATCH_TIME_FOREVER`.

Due to the way that timer dispatch sources are implemented, if a timer passes through a state in which it is due to fire, it may fire even if it’s rescheduled before the event handler is run.  Clients should take care to avoid temporarily scheduling timers in the past.  For example, set the timebase’s rate or time before you set the timer’s next fire time, if you are doing both at once. If setting the timebase’s rate or time might put the timer’s fire time in the past, you may need to set the fire time to `kCMTimeInvalid` across the timebase change.

## See Also

- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](cmtimebaseaddtimer(_:timer:runloop:).md)
  Adds the timer to the list of timers the timebase manages.
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
- [func CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](cmtimebasesettimerdispatchsourcetofireimmediately(_:timersource:).md)
  Sets the timer dispatch source to fire immediately once, overriding any previous timer call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesettimerdispatchsourcenextfiretime(_:timersource:firetime:flags:))*