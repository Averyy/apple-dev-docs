# main

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the run loop of the main thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var main: RunLoop { get }
```

```objc
@property (class, strong, readonly) NSRunLoop * mainRunLoop;
```

## Return Value

An object representing the main thread’s run loop.

## See Also

### Accessing Run Loops and Modes
- [class var current: RunLoop](./current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](./currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](./limitdate%28formode%29.md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [func getCFRunLoop() -> CFRunLoop](./getcfrunloop%28%29.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](./mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/main)*