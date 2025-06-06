# CMTimebaseRemoveTimer(_:timer:)

**Framework**: Core Media  
**Kind**: func

Removes the timer from the list of timers the timebase manages.

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
func CMTimebaseRemoveTimer(_ timebase: CMTimebase, timer: CFRunLoopTimer) -> OSStatus
```

#### Discussion

The timebase no longer maintain the timer’s “NextFireDate.” If the system invalidates the timer, the timebase eventually removes it from its list and releases it even if you don’t call this function.

## See Also

- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](cmtimebaseaddtimer(_:timer:runloop:).md)
  Adds the timer to the list of timers the timebase manages.
- [func CMTimebaseAddTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](cmtimebaseaddtimerdispatchsource(_:timersource:).md)
  Adds the timer dispatch source to the list of timers the timebase manages.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseremovetimer(_:timer:))*