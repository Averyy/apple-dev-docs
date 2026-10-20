# irradiance(atPoint:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGColorRef) irradianceAtPoint:(vector_float3) point;
```

#### Return Value

The color and intensity of the light’s effect on the specified point.

#### Discussion

Calling this method is equivalent to calling the [`irradiance(atPoint:colorSpace:)`](./irradiance%28atpoint,colorspace%29.md) method and passing the Rec. 709 color space. (See `kCGColorSpaceITUR_709`.)

## Parameters

- `point`: A point in the same world coordinate space as the light.

## See Also

### Working with Lights
- [func irradiance(atPoint: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>](./irradiance%28atpoint,colorspace%29.md)
  Returns the radiance of the light as received at a specific point in the same scene, expressed using the specified color space.
- [var lightType: MDLLightType](./lighttype.md)
  The type of the light.
- [var colorSpace: String](./colorspace.md)
  The name of the Core Graphics color space to be used for interpreting the light’s color information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllight/irradiance(atpoint:))*