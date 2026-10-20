# autorepeat

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates how the stepper responds to mouse events.

**Availability**:
- macOS

## Declaration

```swift
var autorepeat: Bool { get set }
```

```objc
@property BOOL autorepeat;
```

#### Discussion

[`true`](../../Swift/true.md) if the first mouse down does one increment (or decrement) and, after a delay of 0.5 seconds, increments (or decrements) at a rate of ten times per second. [`false`](../../Swift/false.md) if the receiver does one increment (decrement) on a mouse up. The default is [`true`](../../Swift/true.md).

## See Also

### Specifying how the stepper responds
- [var valueWraps: Bool](./valuewraps.md)
  A Boolean value that indicates whether the stepper wraps around the minimum and maximum values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstepper/autorepeat)*