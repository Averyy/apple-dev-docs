# CFRunLoopWakeUp(_:)

**Framework**: Core Foundation  
**Kind**: func

Wakes a waiting CFRunLoop object.

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
func CFRunLoopWakeUp(_ rl: CFRunLoop!)
```

#### Discussion

A run loop goes to sleep when it is waiting for a source or timer to become ready to fire. If no source or timer fires, the run loop stays there until it times out or is explicitly woken up. If a run loop is modified, such as a new source added, you need to wake up the run loop to allow it to process the change. Version 0 sources use [`CFRunLoopWakeUp(_:)`](cfrunloopwakeup(_:).md) to cause the run loop to wake up after setting a source to be signaled, if they want the source handled immediately.

## Parameters

- `rl`: The run loop to wake up.

## See Also

- [func CFRunLoopRun()](cfrunlooprun().md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](cfrunloopruninmode(_:_:_:).md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopStop(CFRunLoop!)](cfrunloopstop(_:).md)
  Forces a CFRunLoop object to stop running.
- [func CFRunLoopIsWaiting(CFRunLoop!) -> Bool](cfrunloopiswaiting(_:).md)
  Returns a Boolean value that indicates whether the run loop is waiting for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopwakeup(_:))*