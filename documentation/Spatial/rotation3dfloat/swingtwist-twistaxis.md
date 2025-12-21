# swingTwist(twistAxis:)

**Framework**: Spatial  
**Kind**: method

Returns the rotation’s swing-twist decomposition for a given twist axis.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func swingTwist(twistAxis: RotationAxis3DFloat) -> (swing: Rotation3DFloat, twist: Rotation3DFloat)
```

#### Return Value

A tuple that contains the swing rotation and the twist rotation.

#### Discussion

- Parameter twistAxis The twist axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/swingtwist(twistaxis:))*