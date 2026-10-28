# supportsShaderBarycentricCoordinates

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the GPU supports barycentric coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportsShaderBarycentricCoordinates: Bool { get }
```

```objc
@property (readonly) BOOL supportsShaderBarycentricCoordinates;
```

## Discussion

If a GPU device supports barycentric coordinates, a fragment shader can receive them by adding the `[[barycentric_coord]]` attribute to one of its arguments. See the [Metal Shading Language specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) and [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md) for more information.

## See Also

### Checking render support
- [var supportsRaytracing: Bool](./supportsraytracing.md)
  A Boolean value that indicates whether the GPU device supports ray tracing.
- [var supportsPrimitiveMotionBlur: Bool](./supportsprimitivemotionblur.md)
  A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [var supportsRaytracingFromRender: Bool](./supportsraytracingfromrender.md)
  A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [var supports32BitMSAA: Bool](./supports32bitmsaa.md)
  A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [var supportsPullModelInterpolation: Bool](./supportspullmodelinterpolation.md)
  A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [func supportsVertexAmplificationCount(Int) -> Bool](./supportsvertexamplificationcount%28_%29.md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [var areProgrammableSamplePositionsSupported: Bool](./areprogrammablesamplepositionssupported.md)
  A Boolean value that indicates whether the GPU supports programmable sample positions.
- [var areRasterOrderGroupsSupported: Bool](./arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.
- [var areBarycentricCoordsSupported: Bool](./arebarycentriccoordssupported.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsshaderbarycentriccoordinates)*