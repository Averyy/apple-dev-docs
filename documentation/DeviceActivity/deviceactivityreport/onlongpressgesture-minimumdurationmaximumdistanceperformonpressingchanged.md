# onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)

**Framework**: DeviceActivity  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must   elapse before the gesture succeeds.
- `maximumDistance`: The maximum distance that the fingers or cursor   performing the long press can move before the gesture fails.
- `action`: The action to perform when a long press is recognized.
- `onPressingChanged`: A closure to run when the pressing state of the   gesture changes, passing the current state as a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:))*