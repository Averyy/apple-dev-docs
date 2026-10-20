# CFRunLoopIsWaiting(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the run loop is waiting for an event.

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
func CFRunLoopIsWaiting(_ rl: CFRunLoop!) -> Bool
```

```c
extern Boolean CFRunLoopIsWaiting(CFRunLoopRef rl);
```

#### Return Value

`true` if `rl` has no events to process and is blocking, waiting for a source or timer to become ready to fire; `false` if `rl` either is not running or is currently processing a source, timer, or observer.

#### Discussion

This function is useful only to test the state of another thread’s run loop. When called with the current thread’s run loop, this function always returns `false`.

## Parameters

- `rl`: The run loop to examine.

## See Also

### Starting and Stopping a Run Loop
- [func CFRunLoopRun()](./cfrunlooprun%28%29.md)
  Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [func CFRunLoopRunInMode(CFRunLoopMode!, CFTimeInterval, Bool) -> CFRunLoopRunResult](./cfrunloopruninmode%28_,_,_%29.md)
  Runs the current thread’s CFRunLoop object in a particular mode.
- [func CFRunLoopWakeUp(CFRunLoop!)](./cfrunloopwakeup%28_%29.md)
  Wakes a waiting CFRunLoop object.
- [func CFRunLoopStop(CFRunLoop!)](./cfrunloopstop%28_%29.md)
  Forces a CFRunLoop object to stop running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopiswaiting(_:))*