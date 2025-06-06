# irradiance(atPoint:colorSpace:)

**Framework**: Model I/O  
**Kind**: method

Returns the radiance of the light as received at a specific point in the same scene, expressed using the specified color space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func irradiance(atPoint point: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>
```

#### Return Value

The color and intensity of the light’s effect on the specified point.

## Parameters

- `point`: A point in the same world coordinate space as the light.
- `colorSpace`: The color space in which to interpret the light’s color.

## See Also

- [func irradiance(atPoint: vector_float3) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:).md)
  Returns the radiance of the light as received at a specific point in the same scene.
- [var lightType: MDLLightType](mdllight/lighttype.md)
  The type of the light.
- [var colorSpace: String](mdllight/colorspace.md)
  The name of the Core Graphics color space to be used for interpreting the light’s color information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllight/irradiance(atpoint:colorspace:))*