# currentMode

**Framework**: Foundation  
**Kind**: property

The receiver’s current input mode.

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
var currentMode: RunLoop.Mode? { get }
```

#### Discussion

The receiver’s current input mode. This method returns the current input mode  while the receiver is running; otherwise, it returns `nil`.

The current mode is set by the methods that run the run loop, such as [`acceptInput(forMode:before:)`](runloop/acceptinput(formode:before:).md) and [`run(mode:before:)`](runloop/run(mode:before:).md).

## See Also

- [func run(until: Date)](runloop/run(until:).md)
  Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [func run()](runloop/run.md)
  Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [class var current: RunLoop](runloop/current.md)
  Returns the run loop for the current thread.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](runloop/limitdate(formode:).md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](runloop/main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](runloop/getcfrunloop.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](runloop/mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/currentmode)*