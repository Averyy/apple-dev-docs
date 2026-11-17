# subscript(_:)

**Framework**: ARKit  
**Kind**: subscript  
**Role**: Instance Subscript

Provides the source float triplet at the subscripted index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
subscript(index: Int32) -> (Float, Float, Float) { get }
```

## Return Value

A tuple of three floats.

## Overview

This subscript operates on three-component geometry sources with a [`format`](./format.md) of [`MTLVertexFormat.float3`](../../Metal/mtlvertexformat/float3.md). This operator returns an (x, y, z) offset relative to its parent anchor’s position that corresponds to the subscripted vertex position in [`vertices`](../armeshgeometry/vertices.md) and to the subscripted normal vector in [`normals`](../armeshgeometry/normals.md).

Using this subscript operator leads to a crash if the geometry source has a `.format` other than `MTLVertexFormat.float3`.

## Parameters

- `index`: Index of the element to access.

## See Also

### Accessing Geometry
- [subscript(Int32) -> CUnsignedChar](./subscript%28_%29-7jf4y.md)
  Provides the number at the subscripted index.
- [var buffer: any MTLBuffer](./buffer.md)
  A Metal buffer that contains a list of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/subscript(_:)-3v98f)*