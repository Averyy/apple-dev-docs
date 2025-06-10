# swingTwist(twistAxis:)

**Framework**: Spatial  
**Kind**: method

Returns the rotation’s swing-twist decomposition for a given twist axis.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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