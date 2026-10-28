# setPeriodicDelay(_:interval:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the message delay and interval for the button.

**Availability**:
- macOS

## Declaration

```swift
func setPeriodicDelay(_ delay: Float, interval: Float)
```

```objc
- (void) setPeriodicDelay:(float) delay interval:(float) interval;
```

## Discussion

These values are used if the button is configured (by a [`isContinuous`](../nscell/iscontinuous.md) message) to continuously send the action message to the target object while tracking the mouse.

## Parameters

- `delay`: The amount of time (in seconds) that a continuous button will pause before starting to periodically send action messages to the target object.

  The maximum value is 60.0 seconds; if a larger value is supplied, it’s ignored, and 60.0 seconds is used.
- `interval`: The amount of time (in seconds) between each action message.

  The maximum value is 60.0 seconds; if a larger value is supplied, it’s ignored, and 60.0 seconds is used.

## See Also

### Related Documentation
- [var isContinuous: Bool](../nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
### Managing the Repeat Interval
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./getperiodicdelay%28_,interval%29.md)
  Returns by reference the delay and interval periods for a continuous button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setperiodicdelay(_:interval:))*