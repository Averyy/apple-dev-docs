# maxCameraCount

**Framework**: RealityKit  
**Kind**: property

The maximum number of simultaneous cameras supported.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maxCameraCount: Int { get set }
```

#### Discussion

Must be less than or equal to `CameraArray.maxCount`.

## See Also

- [var rasterSampleCount: Int](lowlevelrenderer/configuration/rastersamplecount.md)
  The number of samples per pixel for MSAA.
- [var enableTonemap: Bool](lowlevelrenderer/configuration/enabletonemap.md)
  A Boolean value that indicates whether output values are tone-mapped to the target pixel format’s range before being written to the output texture.
- [var enableColorMatch: Bool](lowlevelrenderer/configuration/enablecolormatch.md)
  A Boolean value that indicates whether the renderer applies a gamut conversion matrix during resolve, converting from the renderer’s working color space to the output display’s color space.
- [var alphaPremultiply: Bool](lowlevelrenderer/configuration/alphapremultiply.md)
  A Boolean value that indicates whether the renderer divides content by alpha before applying tonemap and color match, then multiplies by alpha before final texture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/maxcameracount)*