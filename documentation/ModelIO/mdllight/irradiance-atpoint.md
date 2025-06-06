# irradiance(atPoint:)

**Framework**: Model I/O  
**Kind**: method

Returns the radiance of the light as received at a specific point in the same scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func irradiance(atPoint point: vector_float3) -> Unmanaged<CGColor>
```

#### Return Value

The color and intensity of the light’s effect on the specified point.

#### Discussion

Calling this method is equivalent to calling the [`irradiance(atPoint:colorSpace:)`](mdllight/irradiance(atpoint:colorspace:).md) method and passing the Rec. 709 color space. (See `kCGColorSpaceITUR_709`.)

## Parameters

- `point`: A point in the same world coordinate space as the light.

## See Also

- [func irradiance(atPoint: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:colorspace:).md)
  Returns the radiance of the light as received at a specific point in the same scene, expressed using the specified color space.
- [var lightType: MDLLightType](mdllight/lighttype.md)
  The type of the light.
- [var colorSpace: String](mdllight/colorspace.md)
  The name of the Core Graphics color space to be used for interpreting the light’s color information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllight/irradiance(atpoint:))*