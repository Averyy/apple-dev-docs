# swing(twistAxis:)

**Framework**: Spatial  
**Kind**: method

Returns the swing component of the rotation’s swing-twist decomposition for a given twist axis.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func swing(twistAxis: RotationAxis3D) -> Rotation3D
```

#### Return Value

The swing component of the rotation’s swing-twist decomposition for a given twist axis.

## Parameters

- `twistAxis`: The twist axis.

## See Also

- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.
- [func swingTwist(twistAxis: RotationAxis3D) -> (swing: Rotation3D, twist: Rotation3D)](rotation3d/swingtwist(twistaxis:).md)
  Returns the rotation’s swing-twist decomposition for a given twist axis.
- [func twist(twistAxis: RotationAxis3D) -> Rotation3D](rotation3d/twist(twistaxis:).md)
  Returns the twist component of the rotation’s swing-twist decomposition for a given twist axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/swing(twistaxis:))*