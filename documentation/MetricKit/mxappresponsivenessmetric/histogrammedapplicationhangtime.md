# histogrammedApplicationHangTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A histogram of the different durations of time in which the app is too busy to handle user interaction responsively.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`HangTimeMetric`](../hangtimemetric.md) instead.

## Declaration

```swift
var histogrammedApplicationHangTime: MXHistogram<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<NSUnitDuration *> * histogrammedApplicationHangTime;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappresponsivenessmetric/histogrammedapplicationhangtime)*