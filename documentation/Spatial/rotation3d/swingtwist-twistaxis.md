# swingTwist(twistAxis:)

**Framework**: Spatial  
**Kind**: method

Returns the rotation’s swing-twist decomposition for a given twist axis.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func swingTwist(twistAxis: RotationAxis3D) -> (swing: Rotation3D, twist: Rotation3D)
```

#### Return Value

A tuple that contains the swing rotation and the twist rotation.

## Parameters

- `twistAxis`: The twist axis.

## See Also

- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/swing(twistaxis:).md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
- [func swing(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/swing(twistaxis:).md)
  Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/swingtwist(twistaxis:))*