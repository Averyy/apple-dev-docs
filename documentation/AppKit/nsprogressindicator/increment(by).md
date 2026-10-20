# increment(by:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Advances the progress bar of a determinate progress indicator by the specified amount.

**Availability**:
- macOS

## Declaration

```swift
func increment(by delta: Double)
```

```objc
- (void) incrementBy:(double) delta;
```

## Parameters

- `delta`: The amount by which to increment the progress bar. For example, if you want to advance a progress bar from 0.0 to 100.0 in 20 steps, you would invoke [`increment(by:)`](./increment%28by%29.md) 20 times with a delta value of 5.0.

## See Also

### Advancing the progress bar
- [var doubleValue: Double](./doublevalue.md)
  The value that indicates the current extent of the progress indicator.
- [var minValue: Double](./minvalue.md)
  The minimum value for the progress indicator.
- [var maxValue: Double](./maxvalue.md)
  The maximum value for the progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/increment(by:))*