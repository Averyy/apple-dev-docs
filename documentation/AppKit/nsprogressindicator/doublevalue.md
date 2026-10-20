# doubleValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The value that indicates the current extent of the progress indicator.

**Availability**:
- macOS

## Declaration

```swift
var doubleValue: Double { get set }
```

```objc
@property double doubleValue;
```

#### Discussion

By default, a determinate progress indicator goes from `0.0` to `100.0`. If the progress bar has advanced halfway across the view, this value would be `50.0`.

An indeterminate progress indicator does not use this value.

## See Also

### Advancing the progress bar
- [func increment(by: Double)](./increment%28by%29.md)
  Advances the progress bar of a determinate progress indicator by the specified amount.
- [var minValue: Double](./minvalue.md)
  The minimum value for the progress indicator.
- [var maxValue: Double](./maxvalue.md)
  The maximum value for the progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/doublevalue)*