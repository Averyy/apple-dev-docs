# increment(by:)

**Framework**: AppKit  
**Kind**: method

Advances the progress bar of a determinate progress indicator by the specified amount.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func increment(by delta: Double)
```

## Parameters

- `delta`: The amount by which to increment the progress bar. For example, if you want to advance a progress bar from 0.0 to 100.0 in 20 steps, you would invoke   20 times with a delta value of 5.0.

## See Also

- [var doubleValue: Double](nsprogressindicator/doublevalue.md)
  The value that indicates the current extent of the progress indicator.
- [var minValue: Double](nsprogressindicator/minvalue.md)
  The minimum value for the progress indicator.
- [var maxValue: Double](nsprogressindicator/maxvalue.md)
  The maximum value for the progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/increment(by:))*