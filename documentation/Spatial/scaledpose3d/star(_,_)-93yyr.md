# *(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Returns the concatenation of a scaled pose and a pose.

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
static func * (lhs: ScaledPose3D, rhs: Pose3D) -> ScaledPose3D
```

## See Also

### Applying arithmetic operations
- [static func * (ScaledPose3D, ScaledPose3D) -> ScaledPose3D](./star%28_,_%29-6nx9h.md)
  Returns the concatenation of two scaled poses.
- [static func * (Pose3D, ScaledPose3D) -> ScaledPose3D](./star%28_,_%29-179zu.md)
  Returns the concatenation of a pose and a scaled pose.
- [static func *= (inout ScaledPose3D, ScaledPose3D)](./stareq%28_,_%29.md)
  Concatenates two scaled poses and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/*(_:_:)-93yyr)*