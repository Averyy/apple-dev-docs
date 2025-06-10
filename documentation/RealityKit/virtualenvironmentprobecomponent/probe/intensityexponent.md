# intensityExponent

**Framework**: RealityKit  
**Kind**: property

The intensity value for the resource, which RealityKit defines on a logarithmic scale.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var intensityExponent: Float
```

#### Discussion

RealityKit multiplies the intensity of the probe by `2^intensityExponent`. An `intensityExponent` of `0.0` means using the diffuse and specular intensities as-is.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/probe/intensityexponent)*