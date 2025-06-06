# ARCoachingOverlayView.Goal.horizontalPlane

**Framework**: ARKit  
**Kind**: case

A goal that specifies your app requires a horizontal plane.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case horizontalPlane
```

#### Discussion

When you use this goal, coaching overlay won’t hide until the user has moved their device in a way that facilitates ARKit finding at least one horizontal surface.

## See Also

- [ARCoachingOverlayView.Goal.anyPlane](arcoachingoverlayview/goal-swift.enum/anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.tracking](arcoachingoverlayview/goal-swift.enum/tracking.md)
  A goal that specifies your app requires basic world tracking.
- [ARCoachingOverlayView.Goal.verticalPlane](arcoachingoverlayview/goal-swift.enum/verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](arcoachingoverlayview/goal-swift.enum/geotracking.md)
  A goal that specifies your app requires a precise geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum/horizontalplane)*