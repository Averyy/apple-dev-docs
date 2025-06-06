# doubleValue

**Framework**: AppKit  
**Kind**: property

The value that indicates the current extent of the progress indicator.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var doubleValue: Double { get set }
```

#### Discussion

By default, a determinate progress indicator goes from `0.0` to `100.0`. If the progress bar has advanced halfway across the view, this value would be `50.0`.

An indeterminate progress indicator does not use this value.

## See Also

- [func increment(by: Double)](nsprogressindicator/increment(by:).md)
  Advances the progress bar of a determinate progress indicator by the specified amount.
- [var minValue: Double](nsprogressindicator/minvalue.md)
  The minimum value for the progress indicator.
- [var maxValue: Double](nsprogressindicator/maxvalue.md)
  The maximum value for the progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/doublevalue)*