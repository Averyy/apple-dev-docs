# MXLaunchTaskID

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

The task identifier to track launch measurements.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`LaunchTaskID`](./launchtaskid.md) instead.

## Declaration

```swift
struct MXLaunchTaskID
```

```c
typedef const NSString * const MXLaunchTaskID;
```

## Topics

### Creating a task identifier
- [init(String)](./mxlaunchtaskid/init%28_%29.md)
  Creates a task identifer from a string.
- [init(rawValue: String)](./mxlaunchtaskid/init%28rawvalue%29.md)
  Creates a task identifer from a string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responsiveness metrics
- [class MXAnimationMetric](./mxanimationmetric.md)
  An object representing metrics about the responsiveness of animation in the app.
- [class MXAppLaunchMetric](./mxapplaunchmetric.md)
  An object representing metrics about app launch time.
- [class MXAppResponsivenessMetric](./mxappresponsivenessmetric.md)
  An object representing metrics about the responsiveness of the app to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxlaunchtaskid)*