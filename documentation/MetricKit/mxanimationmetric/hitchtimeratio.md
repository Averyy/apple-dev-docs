# hitchTimeRatio

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The ratio of time spent hitching during tracked animations.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use [`HitchTimeMetric`](../hitchtimemetric.md) instead.

## Declaration

```swift
var hitchTimeRatio: Measurement<Unit> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * hitchTimeRatio;
```

## Discussion

Hitches are user-perceivable animation issues, such as pauses or jumps that occur during scrolling. This metric incorporates adjustments that optimize for quantifying human perception, and typically is the most accurate representation of hitches people experience during app usage.

Many animations are tracked by default. You can track additional animations using the [`beginActivity(options:reason:)`](../../Foundation/processinfo/beginactivity%28options,reason%29.md) method with the [`animationTrackingEnabled`](../../Foundation/processinfo/activityoptions/animationtrackingenabled.md) option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxanimationmetric/hitchtimeratio)*