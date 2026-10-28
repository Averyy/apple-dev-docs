# ARCoachingOverlayView.Goal.tracking

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

A goal that specifies your app requires basic world tracking.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
case tracking
```

```c
ARCoachingGoalTracking
```

## Discussion

When you use this goal, coaching overlay won’t hide until the user has moved their device in a way that facilitates ARKit starting up a basic world tracking session.

## See Also

### Defining a Goal
- [ARCoachingOverlayView.Goal.anyPlane](./anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.horizontalPlane](./horizontalplane.md)
  A goal that specifies your app requires a horizontal plane.
- [ARCoachingOverlayView.Goal.verticalPlane](./verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](./geotracking.md)
  A goal that specifies your app requires a precise geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum/tracking)*