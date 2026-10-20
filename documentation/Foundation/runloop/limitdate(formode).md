# limitDate(forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.

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
func limitDate(forMode mode: RunLoop.Mode) -> Date?
```

```objc
- (NSDate *) limitDateForMode:(NSRunLoopMode) mode;
```

#### Return Value

The date at which the next timer is scheduled to fire, or `nil` if there are no input sources for this mode.

#### Discussion

The run loop is entered with an immediate timeout, so the run loop does not block, waiting for input, if no input sources need processing.

## Parameters

- `mode`: The run loop mode to search. You may specify custom modes or use one of the modes listed in `Run Loop Modes`.

## See Also

### Accessing Run Loops and Modes
- [class var current: RunLoop](./current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](./currentmode.md)
  The receiver’s current input mode.
- [class var main: RunLoop](./main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](./getcfrunloop%28%29.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](./mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/limitdate(formode:))*