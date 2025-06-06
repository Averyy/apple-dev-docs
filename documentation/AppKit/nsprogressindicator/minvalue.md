# minValue

**Framework**: AppKit  
**Kind**: property

The minimum value for the progress indicator.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var minValue: Double { get set }
```

#### Discussion

By default, a determinate progress indicator goes from `0.0` to `100.0`, so the default value of this property is `0.0`.

An indeterminate progress indicator does not use this value.

## See Also

- [func increment(by: Double)](nsprogressindicator/increment(by:).md)
  Advances the progress bar of a determinate progress indicator by the specified amount.
- [var doubleValue: Double](nsprogressindicator/doublevalue.md)
  The value that indicates the current extent of the progress indicator.
- [var maxValue: Double](nsprogressindicator/maxvalue.md)
  The maximum value for the progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/minvalue)*