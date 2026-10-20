# getCFRunLoop()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s underlying run loop object.

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
func getCFRunLoop() -> CFRunLoop
```

```objc
- (CFRunLoopRef) getCFRunLoop;
```

#### Return Value

The receiver’s underlying [`CFRunLoop`](../../CoreFoundation/cfrunloop.md) object.

#### Discussion

You can use the returned run loop to configure the current run loop using Core Foundation function calls. For example, you might use this function to set up a run loop observer.

## See Also

### Accessing Run Loops and Modes
- [class var current: RunLoop](./current.md)
  Returns the run loop for the current thread.
- [var currentMode: RunLoop.Mode?](./currentmode.md)
  The receiver’s current input mode.
- [func limitDate(forMode: RunLoop.Mode) -> Date?](./limitdate%28formode%29.md)
  Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [class var main: RunLoop](./main.md)
  Returns the run loop of the main thread.
- [RunLoop.Mode](./mode.md)
  Modes that a run loop operates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/getcfrunloop())*