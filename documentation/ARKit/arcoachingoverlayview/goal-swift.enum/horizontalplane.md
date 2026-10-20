# ARCoachingOverlayView.Goal.horizontalPlane

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

A goal that specifies your app requires a horizontal plane.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
case horizontalPlane
```

```c
ARCoachingGoalHorizontalPlane
```

#### Discussion

When you use this goal, coaching overlay won’t hide until the user has moved their device in a way that facilitates ARKit finding at least one horizontal surface.

## See Also

### Defining a Goal
- [ARCoachingOverlayView.Goal.anyPlane](./anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.tracking](./tracking.md)
  A goal that specifies your app requires basic world tracking.
- [ARCoachingOverlayView.Goal.verticalPlane](./verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](./geotracking.md)
  A goal that specifies your app requires a precise geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum/horizontalplane)*