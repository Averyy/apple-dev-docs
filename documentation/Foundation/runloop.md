# RunLoop

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

The programmatic interface to objects that manage input sources.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class RunLoop
```

```objc
@interface NSRunLoop : NSObject
```

## Mentions

- [Processing URL session data task results with Combine](./processing-url-session-data-task-results-with-combine.md)

## Overview

A [`RunLoop`](./runloop.md) object processes input for sources, such as mouse and keyboard events from the window system and [`Port`](./port.md) objects. A [`RunLoop`](./runloop.md) object also processes [`Timer`](./timer.md) events.

Your application neither creates nor explicitly manages [`RunLoop`](./runloop.md) objects. The system creates a [`RunLoop`](./runloop.md) object as needed for each [`Thread`](./thread.md) object, including the application’s main thread. If you need to access the current thread’s run loop, use the class method [`current`](./runloop/current.md).

Note that from the perspective of [`RunLoop`](./runloop.md), [`Timer`](./timer.md) objects aren’t “input”—they’re a special type, and they don’t cause the run loop to return when they fire.

> ⚠️ **Warning**:  The [`RunLoop`](./runloop.md) class is generally not thread-safe, and you must call its methods only within the context of the current thread. Don’t call the methods of a [`RunLoop`](./runloop.md) object running in a different thread, which might cause unexpected results.

## Topics

### Accessing Run Loops and Modes
- [class var current: RunLoop](./runloop/current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](./runloop/currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](./runloop/limitdate%28formode%29.md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](./runloop/main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](./runloop/getcfrunloop%28%29.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](./runloop/mode.md)
  Modes that a run loop operates in.
### Managing Timers
- [func add(Timer, forMode: RunLoop.Mode)](./runloop/add%28_,formode%29-392ag.md)
  Registers a given timer with a given input mode.
### Managing Ports
- [func add(Port, forMode: RunLoop.Mode)](./runloop/add%28_,formode%29-6z982.md)
  Adds a port as an input source to the specified mode of the run loop.
- [func remove(Port, forMode: RunLoop.Mode)](./runloop/remove%28_,formode%29.md)
  Removes a port from the specified input mode of the run loop.
### Running a Loop
- [func run()](./runloop/run%28%29.md)
  Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [func run(mode: RunLoop.Mode, before: Date) -> Bool](./runloop/run%28mode,before%29.md)
  Runs the loop once, blocking for input in the specified mode until a given date.
- [func run(until: Date)](./runloop/run%28until%29.md)
  Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [func acceptInput(forMode: RunLoop.Mode, before: Date)](./runloop/acceptinput%28formode,before%29.md)
  Runs the loop once or until the specified date, accepting input only for the specified mode.
### Scheduling and Canceling Tasks
- [func perform(() -> Void)](./runloop/perform%28_%29.md)
  Schedules a block that the run loop invokes.
- [func perform(inModes: [RunLoop.Mode], block: () -> Void)](./runloop/perform%28inmodes,block%29.md)
  Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](./runloop/perform%28_,target,argument,order,modes%29.md)
  Schedules the sending of a message on the receiver.
- [func cancelPerform(Selector, target: Any, argument: Any?)](./runloop/cancelperform%28_,target,argument%29.md)
  Cancels the sending of a previously scheduled message.
- [func cancelPerformSelectors(withTarget: Any)](./runloop/cancelperformselectors%28withtarget%29.md)
  Cancels all outstanding ordered performs scheduled with a given target.
### Scheduling Combine Publishers
- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](./runloop/schedule%28options,_%29.md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void)](./runloop/schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, using the specified tolerance and options.
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](./runloop/schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](./runloop/minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](./runloop/now.md)
  The run loop scheduler’s definition of the current moment in time.
- [RunLoop.SchedulerTimeType](./runloop/schedulertimetype.md)
  The scheduler time type that the run loop uses.
- [RunLoop.SchedulerOptions](./runloop/scheduleroptions.md)
  A set of options that affect the operation of the run loop scheduler.
### Default Implementations
- [Scheduler Implementations](./runloop/scheduler-implementations.md)
### Configuring as Server Process
- [- configureAsServer](./nsrunloop/configureasserver.md)
  Deprecated. Does nothing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Scheduler](../Combine/scheduler.md)

## See Also

### Run Loop Scheduling
- [class Timer](./timer.md)
  A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop)*