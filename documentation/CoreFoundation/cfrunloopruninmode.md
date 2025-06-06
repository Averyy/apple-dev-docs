# CFRunLoopRunInMode(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Runs the current thread’s CFRunLoop object in a particular mode.

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
func CFRunLoopRunInMode(_ mode: CFRunLoopMode!, _ seconds: CFTimeInterval, _ returnAfterSourceHandled: Bool) -> CFRunLoopRunResult
```

#### Return Value

A value indicating the reason the run loop exited. Possible values are described below.

#### Discussion

Run loops can be run recursively. You can call [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md) from within any run loop callout and create nested run loop activations on the current thread’s call stack. You are not restricted in which modes you can run from within a callout. You can create another run loop activation running in any available run loop mode, including any modes already running higher in the call stack.

The run loop exits with the following return values under the indicated conditions:

- `kCFRunLoopRunFinished`. The run loop mode `mode` has no sources or timers.
- `kCFRunLoopRunStopped`. The run loop was stopped with [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md).
- `kCFRunLoopRunTimedOut`. The time interval `seconds` passed.
- `kCFRunLoopRunHandledSource`. A source was processed. This exit condition only applies when `returnAfterSourceHandled` is `true`.

You must not specify the [`commonModes`](cfrunloopmode/commonmodes.md) constant for the `mode` parameter. Run loops always run in a specific mode. You specify the common modes only when configuring a run-loop observer and only in situations where you want that observer to run in more than one mode.

## Parameters

- `mode`: The run loop mode to run.   can be any arbitrary CFString. You do not need to explicitly create a run loop mode, although a run loop mode needs to contain at least one source or timer to run.
- `seconds`: The length of time to run the run loop. If  , only one pass is made through the run loop before returning; if multiple sources or timers are ready to fire immediately, only one (possibly two if one is a version 0 source) will be fired, regardless of the value of  .
- `returnAfterSourceHandled`: A flag indicating whether the run loop should exit after processing one source. If  , the run loop continues processing events until   has passed.

## See Also

- [func CFRunLoopRun()](cfrunlooprun().md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopWakeUp(CFRunLoop!)](cfrunloopwakeup(_:).md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](cfrunloopstop(_:).md)
  Forces a CFRunLoop object to stop running.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](cfrunloopiswaiting(_:).md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopruninmode(_:_:_:))*