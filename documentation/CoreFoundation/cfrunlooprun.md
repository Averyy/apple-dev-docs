# CFRunLoopRun()

**Framework**: Core Foundation  
**Kind**: func

Runs the current thread’s CFRunLoop object in its default mode indefinitely.

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
func CFRunLoopRun()
```

#### Discussion

The current thread’s run loop runs in the default mode (see [`Default Run Loop Mode`](default-run-loop-mode.md)) until the run loop is stopped with [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md) or all the sources and timers are removed from the default run loop mode.

Run loops can be run recursively. You can call [`CFRunLoopRun()`](cfrunlooprun().md) from within any run loop callout and create nested run loop activations on the current thread’s call stack.

## See Also

- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](cfrunloopruninmode(_:_:_:).md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](cfrunloopwakeup(_:).md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](cfrunloopstop(_:).md)
  Forces a CFRunLoop object to stop running.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](cfrunloopiswaiting(_:).md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprun())*