# CFRunLoop

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFRunLoop
```

#### Overview

A CFRunLoop object monitors sources of input to a task and dispatches control when they become ready for processing. Examples of input sources might include user input devices, network connections, periodic or time-delayed events, and asynchronous callbacks.

Three types of objects can be monitored by a run loop: sources ([`CFRunLoopSource`](cfrunloopsource.md)), timers ([`CFRunLoopTimer`](cfrunlooptimer.md)), and observers ([`CFRunLoopObserver`](cfrunloopobserver.md)). To receive callbacks when these objects need processing, you must first place these objects into a run loop with [`CFRunLoopAddSource(_:_:_:)`](cfrunloopaddsource(_:_:_:).md), [`CFRunLoopAddTimer(_:_:_:)`](cfrunloopaddtimer(_:_:_:).md), or [`CFRunLoopAddObserver(_:_:_:)`](cfrunloopaddobserver(_:_:_:).md). You can later remove an object from the run loop (or invalidate it) to stop receiving its callback.

Each source, timer, and observer added to a run loop must be associated with one or more run loop modes. Modes determine what events are processed by the run loop during a given iteration. Each time the run loop executes, it does so in a specific mode. While in that mode, the run loop processes only the events associated with sources, timers, and observers associated with that mode. You assign most sources to the default run loop mode (designated by the [`defaultMode`](cfrunloopmode/defaultmode.md) constant), which is used to process events when the application (or thread) is idle. However, the system defines other modes and may execute the run loop in those other modes to limit which sources, timers, and observers are processed. Because run-loop modes are simply specified as strings, you can also define your own custom modes to limit the processing of events

Core Foundation defines a special pseudo-mode, called the common modes, that allow you to associate more than one mode with a given source, timer, or observer. To specify the common modes, use the [`commonModes`](cfrunloopmode/commonmodes.md) constant for the mode when configuring the object. Each run loop has its own independent set of common modes and the default mode ([`defaultMode`](cfrunloopmode/defaultmode.md)) is always a member of the set. To add a mode to the set of common modes, use the [`CFRunLoopAddCommonMode(_:_:)`](cfrunloopaddcommonmode(_:_:).md) function.

There is exactly one run loop per thread. You neither create nor destroy a thread’s run loop. Core Foundation automatically creates it for you as needed. You obtain the current thread’s run loop with [`CFRunLoopGetCurrent()`](cfrunloopgetcurrent().md). Call [`CFRunLoopRun()`](cfrunlooprun().md) to run the current thread’s run loop in the default mode until the run loop is stopped with [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md). You can also call [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md) to run the current thread’s run loop in a specified mode for a set period of time (or until the run loop is stopped). A run loop can only run if the requested mode has at least one source or timer to monitor.

Run loops can be run recursively. You can call [`CFRunLoopRun()`](cfrunlooprun().md) or [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md) from within any run loop callout and create nested run loop activations on the current thread’s call stack. You are not restricted in which modes you can run from within a callout. You can create another run loop activation running in any available run loop mode, including any modes already running higher in the call stack.

Cocoa applications build upon CFRunLoop to implement their own higher-level event loop. When writing an application, you can add your sources, timers, and observers to their run loop objects and modes. Your objects will then get monitored as part of the regular application event loop. Use the [`getCFRunLoop()`](https://developer.apple.com/documentation/foundation/runloop/1410140-getcfrunloop) method of [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop) to obtain the corresponding [`CFRunLoop`](cfrunloop.md) type. In Carbon applications, use the `GetCFRunLoopFromEventLoop` function.

For more information about how run loops behave, see [`Run Loops`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16) in [`Threading Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## Topics

### Getting a Run Loop
- [func CFRunLoopGetCurrent() -> CFRunLoop!](cfrunloopgetcurrent().md)
  Returns the CFRunLoop object for the current thread.
- [func CFRunLoopGetMain() -> CFRunLoop!](cfrunloopgetmain().md)
  Returns the main CFRunLoop object.
### Starting and Stopping a Run Loop
- [func CFRunLoopRun()](cfrunlooprun().md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](cfrunloopruninmode(_:_:_:).md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](cfrunloopwakeup(_:).md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](cfrunloopstop(_:).md)
  Forces a CFRunLoop object to stop running.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](cfrunloopiswaiting(_:).md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.
### Managing Sources
- [func CFRunLoopAddSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopaddsource(_:_:_:).md)
  Adds a CFRunLoopSource object to a run loop mode.
- [func CFRunLoopContainsSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!) -> Bool](cfrunloopcontainssource(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.
- [func CFRunLoopRemoveSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopremovesource(_:_:_:).md)
  Removes a CFRunLoopSource object from a run loop mode.
### Managing Observers
- [func CFRunLoopAddObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](cfrunloopaddobserver(_:_:_:).md)
  Adds a CFRunLoopObserver object to a run loop mode.
- [func CFRunLoopContainsObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!) -> Bool](cfrunloopcontainsobserver(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.
- [func CFRunLoopRemoveObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](cfrunloopremoveobserver(_:_:_:).md)
  Removes a CFRunLoopObserver object from a run loop mode.
### Managing Run Loop Modes
- [func CFRunLoopAddCommonMode(CFRunLoop!, CFRunLoopMode!)](cfrunloopaddcommonmode(_:_:).md)
  Adds a mode to the set of run loop common modes.
- [func CFRunLoopCopyAllModes(CFRunLoop!) -> CFArray!](cfrunloopcopyallmodes(_:).md)
  Returns an array that contains all the defined modes for a CFRunLoop object.
- [func CFRunLoopCopyCurrentMode(CFRunLoop!) -> CFRunLoopMode!](cfrunloopcopycurrentmode(_:).md)
  Returns the name of the mode in which a given run loop is currently running.
### Managing Timers
- [func CFRunLoopAddTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](cfrunloopaddtimer(_:_:_:).md)
  Adds a CFRunLoopTimer object to a run loop mode.
- [func CFRunLoopGetNextTimerFireDate(CFRunLoop!, CFRunLoopMode!) -> CFAbsoluteTime](cfrunloopgetnexttimerfiredate(_:_:).md)
  Returns the time at which the next timer will fire.
- [func CFRunLoopRemoveTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](cfrunloopremovetimer(_:_:_:).md)
  Removes a CFRunLoopTimer object from a run loop mode.
- [func CFRunLoopContainsTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!) -> Bool](cfrunloopcontainstimer(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.
### Scheduling Blocks
- [func CFRunLoopPerformBlock(CFRunLoop!, CFTypeRef!, (() -> Void)!)](cfrunloopperformblock(_:_:_:).md)
  Enqueues a block object on a given runloop to be executed as the runloop cycles in specified modes.
### Getting the CFRunLoop Type ID
- [func CFRunLoopGetTypeID() -> CFTypeID](cfrunloopgettypeid().md)
  Returns the type identifier for the CFRunLoop opaque type.
### Constants
- [CFRunLoopRunInMode Exit Codes](cfrunloopruninmode_exit_codes.md)
  Return codes for `CFRunLoopRunInMode`, identifying the reason the run loop exited.
- [Common Mode Flag](common-mode-flag.md)
  A run loop pseudo-mode that manages objects monitored in the “common” modes.
- [Default Run Loop Mode](default-run-loop-mode.md)
  Default run loop mode.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloop)*