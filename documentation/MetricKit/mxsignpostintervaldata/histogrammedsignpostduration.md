# histogrammedSignpostDuration

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

A histogram of the different time intervals of a custom metric event.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`signpostDuration`](../signpostintervalmetric/signpostduration.md) instead.

## Declaration

```swift
var histogrammedSignpostDuration: MXHistogram<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) MXHistogram<NSUnitDuration *> * histogrammedSignpostDuration;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostintervaldata/histogrammedsignpostduration)*