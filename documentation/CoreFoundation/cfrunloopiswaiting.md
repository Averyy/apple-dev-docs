# CFRunLoopIsWaiting(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether the run loop is waiting for an event.

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
func CFRunLoopIsWaiting(_ rl: CFRunLoop!) -> Bool
```

#### Return Value

`true` if `rl` has no events to process and is blocking, waiting for a source or timer to become ready to fire; `false` if `rl` either is not running or is currently processing a source, timer, or observer.

#### Discussion

This function is useful only to test the state of another thread’s run loop. When called with the current thread’s run loop, this function always returns `false`.

## Parameters

- `rl`: The run loop to examine.

## See Also

- [func CFRunLoopRun()](cfrunlooprun().md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](cfrunloopruninmode(_:_:_:).md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](cfrunloopwakeup(_:).md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](cfrunloopstop(_:).md)
  Forces a CFRunLoop object to stop running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopiswaiting(_:))*