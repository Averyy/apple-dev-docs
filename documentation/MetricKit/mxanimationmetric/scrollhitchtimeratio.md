# scrollHitchTimeRatio

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The ratio of the time spent hitching while scrolling.

**Availability**:
- iOS 14.0+ - Deprecated in 27.3
- iPadOS 14.0+ - Deprecated in 27.3
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Use [`HitchTimeMetric`](../hitchtimemetric.md) instead.

## Declaration

```swift
var scrollHitchTimeRatio: Measurement<Unit> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * scrollHitchTimeRatio;
```

## Discussion

Hitches are user-perceivable animation issues, such as pauses or jumps that occur during scrolling.

> **Note**:  This metric applies only to scrolling in UIScrollView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxanimationmetric/scrollhitchtimeratio)*