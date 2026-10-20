# areBarycentricCoordsSupported

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the GPU supports barycentric coordinates.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`supportsShaderBarycentricCoordinates`](./supportsshaderbarycentriccoordinates.md) instead.

## Declaration

```swift
var areBarycentricCoordsSupported: Bool { get }
```

```objc
@property (readonly, getter=areBarycentricCoordsSupported) BOOL barycentricCoordsSupported;
```

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
- [var supportsShaderBarycentricCoordinates: Bool](./supportsshaderbarycentriccoordinates.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [func supportsVertexAmplificationCount(Int) -> Bool](./supportsvertexamplificationcount%28_%29.md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [var areProgrammableSamplePositionsSupported: Bool](./areprogrammablesamplepositionssupported.md)
  A Boolean value that indicates whether the GPU supports programmable sample positions.
- [var areRasterOrderGroupsSupported: Bool](./arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/arebarycentriccoordssupported)*