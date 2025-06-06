# supportsRaytracingFromRender

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportsRaytracingFromRender: Bool { get }
```

## See Also

- [var supportsRaytracing: Bool](mtldevice/supportsraytracing.md)
  A Boolean value that indicates whether the GPU device supports ray tracing.
- [var supportsPrimitiveMotionBlur: Bool](mtldevice/supportsprimitivemotionblur.md)
  A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [var supports32BitMSAA: Bool](mtldevice/supports32bitmsaa.md)
  A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [var supportsPullModelInterpolation: Bool](mtldevice/supportspullmodelinterpolation.md)
  A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [var supportsShaderBarycentricCoordinates: Bool](mtldevice/supportsshaderbarycentriccoordinates.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [func supportsVertexAmplificationCount(Int) -> Bool](mtldevice/supportsvertexamplificationcount(_:).md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [var areProgrammableSamplePositionsSupported: Bool](mtldevice/areprogrammablesamplepositionssupported.md)
  A Boolean value that indicates whether the GPU supports programmable sample positions.
- [var areRasterOrderGroupsSupported: Bool](mtldevice/arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.
- [var areBarycentricCoordsSupported: Bool](mtldevice/arebarycentriccoordssupported.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsraytracingfromrender)*