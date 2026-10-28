# CFRunLoopRun()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Runs the current thread’s CFRunLoop object in its default mode indefinitely.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFRunLoopRun()
```

```c
extern void CFRunLoopRun();
```

## Discussion

The current thread’s run loop runs in the default mode (see [Default Run Loop Mode](./default-run-loop-mode.md)) until the run loop is stopped with [`CFRunLoopStop(_:)`](./cfrunloopstop%28_%29.md) or all the sources and timers are removed from the default run loop mode.

Run loops can be run recursively. You can call [`CFRunLoopRun()`](./cfrunlooprun%28%29.md) from within any run loop callout and create nested run loop activations on the current thread’s call stack.

## See Also

### Starting and Stopping a Run Loop
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](./cfrunloopruninmode%28_,_,_%29.md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](./cfrunloopwakeup%28_%29.md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](./cfrunloopstop%28_%29.md)
  Forces a CFRunLoop object to stop running.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](./cfrunloopiswaiting%28_%29.md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprun())*