# areProgrammableSamplePositionsSupported

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the GPU supports programmable sample positions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var areProgrammableSamplePositionsSupported: Bool { get }
```

## Mentions

- [Positioning samples programmatically](positioning-samples-programmatically.md)
- [Storing data a pass makes with custom sample positions for a subsequent pass](storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

## See Also

- [var supportsRaytracing: Bool](mtldevice/supportsraytracing.md)
  A Boolean value that indicates whether the GPU device supports ray tracing.
- [var supportsPrimitiveMotionBlur: Bool](mtldevice/supportsprimitivemotionblur.md)
  A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [var supportsRaytracingFromRender: Bool](mtldevice/supportsraytracingfromrender.md)
  A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [var supports32BitMSAA: Bool](mtldevice/supports32bitmsaa.md)
  A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [var supportsPullModelInterpolation: Bool](mtldevice/supportspullmodelinterpolation.md)
  A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [var supportsShaderBarycentricCoordinates: Bool](mtldevice/supportsshaderbarycentriccoordinates.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [func supportsVertexAmplificationCount(Int) -> Bool](mtldevice/supportsvertexamplificationcount(_:).md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [var areRasterOrderGroupsSupported: Bool](mtldevice/arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.
- [var areBarycentricCoordsSupported: Bool](mtldevice/arebarycentriccoordssupported.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/areprogrammablesamplepositionssupported)*