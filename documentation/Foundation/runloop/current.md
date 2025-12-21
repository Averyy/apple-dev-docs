# current

**Framework**: Foundation  
**Kind**: property

Returns the run loop for the current thread.

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
class var current: RunLoop { get }
```

#### Return Value

The `NSRunLoop` object for the current thread.

#### Discussion

If a run loop does not yet exist for the thread, one is created and returned.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [var currentMode: RunLoop.Mode?](runloop/currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](runloop/limitdate(formode:).md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](runloop/main.md)
  Returns the run loop of the main thread.
- [func getCFRunLoop() -> CFRunLoop](runloop/getcfrunloop.md)
  Returns the receiver’s underlying run loop object.
- [RunLoop.Mode](runloop/mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/current)*