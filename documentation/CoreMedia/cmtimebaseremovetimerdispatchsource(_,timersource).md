# CMTimebaseRemoveTimerDispatchSource(_:timerSource:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Removes the timer dispatch source from the list of timers the timebase manages.

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
func CMTimebaseRemoveTimerDispatchSource(_ timebase: CMTimebase, timerSource: dispatch_source_t) -> OSStatus
```

```c
extern OSStatus CMTimebaseRemoveTimerDispatchSource(CMTimebaseRef timebase, dispatch_source_t timerSource);
```

## Discussion

The timebase no longer maintains the timer source’s start time. If the system cancels the timer source, the timebase eventually removes it from its list and releases it even if you don’t call this function.

## See Also

### Interacting with Timers
- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](./cmtimebaseaddtimer%28_,timer,runloop%29.md)
  Adds the timer to the list of timers the timebase manages.
- [func CMTimebaseAddTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebaseaddtimerdispatchsource%28_,timersource%29.md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func CMTimebaseRemoveTimer(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebaseremovetimer%28_,timer%29.md)
  Removes the timer from the list of timers the timebase manages.
- [func CMTimebaseSetTimerNextFireTime(CMTimebase, timer: CFRunLoopTimer, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimernextfiretime%28_,timer,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func CMTimebaseSetTimerToFireImmediately(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebasesettimertofireimmediately%28_,timer%29.md)
  Sets the timer to fire immediately once, overriding any previous timer calls.
- [func CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase, timerSource: dispatch_source_t, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimerdispatchsourcenextfiretime%28_,timersource,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebasesettimerdispatchsourcetofireimmediately%28_,timersource%29.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous timer call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseremovetimerdispatchsource(_:timersource:))*