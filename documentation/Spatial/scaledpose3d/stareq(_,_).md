# *=(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Concatenates two scaled poses and stores the result in the left-hand-side variable.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
static func *= (lhs: inout ScaledPose3D, rhs: ScaledPose3D)
```

## See Also

### Applying arithmetic operations
- [static func * (ScaledPose3D, ScaledPose3D) -> ScaledPose3D](./star%28_,_%29-6nx9h.md)
  Returns the concatenation of two scaled poses.
- [static func * (ScaledPose3D, Pose3D) -> ScaledPose3D](./star%28_,_%29-93yyr.md)
  Returns the concatenation of a scaled pose and a pose.
- [static func * (Pose3D, ScaledPose3D) -> ScaledPose3D](./star%28_,_%29-179zu.md)
  Returns the concatenation of a pose and a scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/*=(_:_:))*