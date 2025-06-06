# colorSpace

**Framework**: Model I/O  
**Kind**: property

The name of the Core Graphics color space to be used for interpreting the light’s color information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorSpace: String { get set }
```

## See Also

- [func irradiance(atPoint: vector_float3) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:).md)
  Returns the radiance of the light as received at a specific point in the same scene.
- [func irradiance(atPoint: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:colorspace:).md)
  Returns the radiance of the light as received at a specific point in the same scene, expressed using the specified color space.
- [var lightType: MDLLightType](mdllight/lighttype.md)
  The type of the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllight/colorspace)*