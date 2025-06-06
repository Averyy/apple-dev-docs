# CFRunLoopStop(_:)

**Framework**: Core Foundation  
**Kind**: func

Forces a CFRunLoop object to stop running.

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
func CFRunLoopStop(_ rl: CFRunLoop!)
```

#### Discussion

This function forces `rl` to stop running and return control to the function that called [`CFRunLoopRun()`](cfrunlooprun().md) or [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md) for the current run loop activation. If the run loop is nested with a callout from one activation starting another activation running, only the innermost activation is exited.

## Parameters

- `rl`: The run loop to stop.

## See Also

- [func CFRunLoopRun()](cfrunlooprun().md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](cfrunloopruninmode(_:_:_:).md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](cfrunloopwakeup(_:).md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](cfrunloopiswaiting(_:).md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopstop(_:))*