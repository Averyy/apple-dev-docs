# CMTimebaseAddTimerDispatchSource(_:timerSource:)

**Framework**: Core Media  
**Kind**: func

Adds the timer dispatch source to the list of timers the timebase manages.

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
func CMTimebaseAddTimerDispatchSource(_ timebase: CMTimebase, timerSource: dispatch_source_t) -> OSStatus
```

#### Discussion

You must create the timer source by calling `dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, some_dispatch_queue)` and associate an event handler with it from `dispatch_source_set_event_handler(timerSource, some_handler_block)` or `dispatch_source_set_event_handler_f(timerSource, some_handler_function)`. Call `dispatch_resume(timerSource)` because the system creates dispatch sources in a suspended state.

The timebase retains the timer source, and maintains its start time according to the `CMTime` set using [`CMTimebaseSetTimerDispatchSourceNextFireTime(_:timerSource:fireTime:flags:)`](cmtimebasesettimerdispatchsourcenextfiretime(_:timersource:firetime:flags:).md). Until the first call to [`CMTimebaseSetTimerDispatchSourceNextFireTime(_:timerSource:fireTime:flags:)`](cmtimebasesettimerdispatchsourcenextfiretime(_:timersource:firetime:flags:).md), the system sets the start time to `DISPATCH_TIME_FOREVER`.

For more information on dispatch sources, see [`Dispatch Sources`](https://developer.apple.comhttp://developer.apple.com/library/mac/#DOCUMENTATION/General/Conceptual/ConcurrencyProgrammingGuide/GCDWorkQueues/GCDWorkQueues.html).

## See Also

- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](cmtimebaseaddtimer(_:timer:runloop:).md)
  Adds the timer to the list of timers the timebase manages.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseaddtimerdispatchsource(_:timersource:))*