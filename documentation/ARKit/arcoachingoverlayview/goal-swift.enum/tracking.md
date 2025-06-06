# ARCoachingOverlayView.Goal.tracking

**Framework**: ARKit  
**Kind**: case

A goal that specifies your app requires basic world tracking.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case tracking
```

#### Discussion

When you use this goal, coaching overlay won’t hide until the user has moved their device in a way that facilitates ARKit starting up a basic world tracking session.

## See Also

- [ARCoachingOverlayView.Goal.anyPlane](arcoachingoverlayview/goal-swift.enum/anyplane.md)
  A goal that specifies your app requires a plane of any type.
- [ARCoachingOverlayView.Goal.horizontalPlane](arcoachingoverlayview/goal-swift.enum/horizontalplane.md)
  A goal that specifies your app requires a horizontal plane.
- [ARCoachingOverlayView.Goal.verticalPlane](arcoachingoverlayview/goal-swift.enum/verticalplane.md)
  A goal that specifies your app requires a vertical plane.
- [ARCoachingOverlayView.Goal.geoTracking](arcoachingoverlayview/goal-swift.enum/geotracking.md)
  A goal that specifies your app requires a precise geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/goal-swift.enum/tracking)*