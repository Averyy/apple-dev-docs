# intensityExponent

**Framework**: RealityKit  
**Kind**: property

The intensity value of the light, defined on a logarithmic scale.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
var intensityExponent: Float
```

#### Discussion

An intensity factor is computed as `2^intensityExponent`. The computed value modulates the native value specified in the diffuse and specular textures.

Set the intensity to `0` to result in a scale factor of `1`. This uses the unmodified texture’s diffuse and specular intensities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct/imagebasedlight/intensityexponent)*