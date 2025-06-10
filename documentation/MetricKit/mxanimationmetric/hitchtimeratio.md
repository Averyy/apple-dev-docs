# hitchTimeRatio

**Framework**: MetricKit  
**Kind**: property

The ratio of time spent hitching during tracked animations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var hitchTimeRatio: Measurement<Unit> { get }
```

#### Discussion

Hitches are user-perceivable animation issues, such as pauses or jumps that occur during scrolling. This metric incorporates adjustments that optimize for quantifying human perception, and typically is the most accurate representation of hitches people experience during app usage.

Many animations are tracked by default. You can track additional animations using the [`beginActivity(options:reason:)`](https://developer.apple.com/documentation/Foundation/ProcessInfo/beginActivity(options:reason:)) method with the [`animationTrackingEnabled`](https://developer.apple.com/documentation/Foundation/ProcessInfo/ActivityOptions/animationTrackingEnabled) option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxanimationmetric/hitchtimeratio)*