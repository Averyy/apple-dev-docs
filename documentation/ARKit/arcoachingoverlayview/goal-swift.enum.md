# ARCoachingOverlayView.Goal

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The options that specify your app’s tracking requirements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
enum Goal
```

```c
enum ARCoachingGoal : NSInteger;
```

## Overview

This property contains the available options when you set a coaching overlay’s [`goal`](./goal-swift.property.md). The coaching overlay adjusts its messaging to the user based on the value.

## Topics

### Defining a Goal
- [ARCoachingOverlayView.Goal.anyPlane](./goal-swift.enum/anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.horizontalPlane](./goal-swift.enum/horizontalplane.md)
  A goal that specifies your app requires a horizontal plane.
- [ARCoachingOverlayView.Goal.tracking](./goal-swift.enum/tracking.md)
  A goal that specifies your app requires basic world tracking.
- [ARCoachingOverlayView.Goal.verticalPlane](./goal-swift.enum/verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](./goal-swift.enum/geotracking.md)
  A goal that specifies your app requires a precise geographic location.
### Initializers
- [init?(rawValue: Int)](./goal-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining a Goal
- [var goal: ARCoachingOverlayView.Goal](./goal-swift.property.md)
  A field that indicates your app’s tracking requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum)*