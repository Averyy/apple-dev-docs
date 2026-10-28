# supportsVertexAmplificationCount(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the GPU supports an amplification factor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func supportsVertexAmplificationCount(_ count: Int) -> Bool
```

```objc
- (BOOL) supportsVertexAmplificationCount:(NSUInteger) count;
```

## Mentions

- [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md)

## Discussion

A vertex amplification factor of `1` has no effect because it effectively disables vertex amplification.

> ❗ **Important**:  Passing a vertex amplification factor of `1` or less to this method triggers an API validation error.

For more information about vertex amplification, see [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md).

## Parameters

- `count`: An integer that represents the number of output streams you want the GPU to generate from an input stream.

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
- [var areProgrammableSamplePositionsSupported: Bool](./areprogrammablesamplepositionssupported.md)
  A Boolean value that indicates whether the GPU supports programmable sample positions.
- [var areRasterOrderGroupsSupported: Bool](./arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.
- [var areBarycentricCoordsSupported: Bool](./arebarycentriccoordssupported.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/supportsvertexamplificationcount(_:))*