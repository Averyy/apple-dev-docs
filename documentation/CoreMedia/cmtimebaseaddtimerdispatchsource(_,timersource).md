# CMTimebaseAddTimerDispatchSource(_:timerSource:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CMTimebaseAddTimerDispatchSource(CMTimebaseRef timebase, dispatch_source_t timerSource);
```

#### Discussion

You must create the timer source by calling `dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, some_dispatch_queue)` and associate an event handler with it from `dispatch_source_set_event_handler(timerSource, some_handler_block)` or `dispatch_source_set_event_handler_f(timerSource, some_handler_function)`. Call `dispatch_resume(timerSource)` because the system creates dispatch sources in a suspended state.

The timebase retains the timer source, and maintains its start time according to the `CMTime` set using [`CMTimebaseSetTimerDispatchSourceNextFireTime(_:timerSource:fireTime:flags:)`](./cmtimebasesettimerdispatchsourcenextfiretime%28_,timersource,firetime,flags%29.md). Until the first call to [`CMTimebaseSetTimerDispatchSourceNextFireTime(_:timerSource:fireTime:flags:)`](./cmtimebasesettimerdispatchsourcenextfiretime%28_,timersource,firetime,flags%29.md), the system sets the start time to `DISPATCH_TIME_FOREVER`.

For more information on dispatch sources, see [Dispatch Sources](http://developer.apple.com/library/mac/#DOCUMENTATION/General/Conceptual/ConcurrencyProgrammingGuide/GCDWorkQueues/GCDWorkQueues.html).

## See Also

### Interacting with Timers
- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](./cmtimebaseaddtimer%28_,timer,runloop%29.md)
  Adds the timer to the list of timers the timebase manages.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebaseaddtimerdispatchsource(_:timersource:))*