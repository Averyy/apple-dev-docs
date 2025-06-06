# ARCoachingOverlayView.Goal.anyPlane

**Framework**: ARKit  
**Kind**: case

A goal that specifies your app requires a plane of any type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case anyPlane
```

#### Discussion

When you use this goal, coaching overlay won’t hide until the user has moved their device in a way that facilitates ARKit finding at least one surface. For the available surface types, see [`ARPlaneClassification`](arplaneclassification.md).

## See Also

- [ARCoachingOverlayView.Goal.horizontalPlane](arcoachingoverlayview/goal-swift.enum/horizontalplane.md)
  A goal that specifies your app requires a horizontal plane.
- [ARCoachingOverlayView.Goal.tracking](arcoachingoverlayview/goal-swift.enum/tracking.md)
  A goal that specifies your app requires basic world tracking.
- [ARCoachingOverlayView.Goal.verticalPlane](arcoachingoverlayview/goal-swift.enum/verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](arcoachingoverlayview/goal-swift.enum/geotracking.md)
  A goal that specifies your app requires a precise geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum/anyplane)*