# getPeriodicDelay(_:interval:)

**Framework**: AppKit  
**Kind**: method

Returns by reference the delay and interval periods for a continuous button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func getPeriodicDelay(_ delay: UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)
```

## Parameters

- `delay`: On return, the amount of time (in seconds) that the button will pause before starting to periodically send action messages to the target object. Default values are taken from the user’s defaults (60 seconds maximum); if the user hasn’t specified a default value, this defaults to 0.4 seconds.
- `interval`: On return, the amount of time (in seconds) between each action message. Default values are taken from the user’s defaults (60 seconds maximum); if the user hasn’t specified a default value, this defaults to 0.075 seconds.

## See Also

- [var isContinuous: Bool](nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func setPeriodicDelay(Float, interval: Float)](nsbuttoncell/setperiodicdelay(_:interval:).md)
  Sets the message delay and interval for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/getperiodicdelay(_:interval:))*