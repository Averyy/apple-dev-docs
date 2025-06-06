# setPeriodicDelay(_:interval:)

**Framework**: AppKit  
**Kind**: method

Sets the message delay and interval for the button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setPeriodicDelay(_ delay: Float, interval: Float)
```

#### Discussion

These values are used if the button is configured (by a [`isContinuous`](nscell/iscontinuous.md) message) to continuously send the action message to the target object while tracking the mouse.

## Parameters

- `delay`: The maximum value is 60.0 seconds; if a larger value is supplied, it’s ignored, and 60.0 seconds is used.
- `interval`: The maximum value is 60.0 seconds; if a larger value is supplied, it’s ignored, and 60.0 seconds is used.

## See Also

- [var isContinuous: Bool](nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](nsbuttoncell/getperiodicdelay(_:interval:).md)
  Returns by reference the delay and interval periods for a continuous button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setperiodicdelay(_:interval:))*