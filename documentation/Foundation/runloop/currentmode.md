# currentMode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSRunLoopMode currentMode;
```

## Discussion

The receiver’s current input mode. This method returns the current input mode *only* while the receiver is running; otherwise, it returns `nil`.

The current mode is set by the methods that run the run loop, such as [`acceptInput(forMode:before:)`](./acceptinput%28formode,before%29.md) and [`run(mode:before:)`](./run%28mode,before%29.md).

## See Also

### Related Documentation
- [func run(until: Date)](./run%28until%29.md)
  Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [func run()](./run%28%29.md)
  Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
### Accessing Run Loops and Modes
- [class var current: RunLoop](./current.md)
  Returns the run loop for the current thread.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](./limitdate%28formode%29.md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](./main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](./getcfrunloop%28%29.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](./mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/currentmode)*