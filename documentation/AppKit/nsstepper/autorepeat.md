# autorepeat

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates how the stepper responds to mouse events.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autorepeat: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the first mouse down does one increment (or decrement) and, after a delay of 0.5 seconds, increments (or decrements) at a rate of ten times per second. [`false`](https://developer.apple.com/documentation/Swift/false) if the receiver does one increment (decrement) on a mouse up. The default is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var valueWraps: Bool](nsstepper/valuewraps.md)
  A Boolean value that indicates whether the stepper wraps around the minimum and maximum values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstepper/autorepeat)*