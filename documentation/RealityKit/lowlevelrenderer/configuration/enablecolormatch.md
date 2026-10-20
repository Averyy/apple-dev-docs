# enableColorMatch

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the renderer applies a gamut conversion matrix during resolve, converting from the renderer’s working color space to the output display’s color space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var enableColorMatch: Bool { get set }
```

## See Also

### Tuning rendering options
- [var rasterSampleCount: Int](./rastersamplecount.md)
  The number of samples per pixel for MSAA.
- [var enableTonemap: Bool](./enabletonemap.md)
  A Boolean value that indicates whether output values are tone-mapped to the target pixel format’s range before being written to the output texture.
- [var alphaPremultiply: Bool](./alphapremultiply.md)
  A Boolean value that indicates whether the renderer divides content by alpha before applying tonemap and color match, then multiplies by alpha before final texture output.
- [var maxCameraCount: Int](./maxcameracount.md)
  The maximum number of simultaneous cameras supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/enablecolormatch)*