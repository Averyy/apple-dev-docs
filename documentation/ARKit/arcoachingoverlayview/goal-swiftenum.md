# ARCoachingOverlayView.Goal

**Framework**: ARKit  
**Kind**: enum

The options that specify your app’s tracking requirements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Goal
```

#### Overview

This property contains the available options when you set a coaching overlay’s [`goal`](arcoachingoverlayview/goal-swift.property.md). The coaching overlay adjusts its messaging to the user based on the value.

## Topics

### Defining a Goal
- [ARCoachingOverlayView.Goal.anyPlane](arcoachingoverlayview/goal-swift.enum/anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.horizontalPlane](arcoachingoverlayview/goal-swift.enum/horizontalplane.md)
  A goal that specifies your app requires a horizontal plane.
- [ARCoachingOverlayView.Goal.tracking](arcoachingoverlayview/goal-swift.enum/tracking.md)
  A goal that specifies your app requires basic world tracking.
- [ARCoachingOverlayView.Goal.verticalPlane](arcoachingoverlayview/goal-swift.enum/verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](arcoachingoverlayview/goal-swift.enum/geotracking.md)
  A goal that specifies your app requires a precise geographic location.
### Initializers
- [init?(rawValue: Int)](arcoachingoverlayview/goal-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var goal: ARCoachingOverlayView.Goal](arcoachingoverlayview/goal-swift.property.md)
  A field that indicates your app’s tracking requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum)*