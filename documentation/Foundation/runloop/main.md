# main

**Framework**: Foundation  
**Kind**: property

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

#### Return Value

An object representing the main thread’s run loop.

## See Also

- [class var current: RunLoop](runloop/current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](runloop/currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](runloop/limitdate(formode:).md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [func getCFRunLoop() -> CFRunLoop](runloop/getcfrunloop.md)
  Returns the receiver’s underlying [`CFRunLoop`](https://developer.apple.com/documentation/CoreFoundation/CFRunLoop) object.
- [RunLoop.Mode](runloop/mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/main)*