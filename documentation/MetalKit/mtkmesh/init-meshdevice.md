# init(mesh:device:)

**Framework**: Metalkit  
**Kind**: init

Initializes a MetalKit mesh and its submeshes from a Model I/O mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mesh: MDLMesh, device: any MTLDevice) throws
```

#### Return Value

A new MetalKit mesh object, or `nil` if an error occured.

#### Discussion

This initializer does  initialize any children meshes of the Model I/O mesh.

All vertex buffers in the source Model I/O mesh and the index buffer of each of its submeshes must have been created with a [`MTKMeshBufferAllocator`](mtkmeshbufferallocator.md) object.

A Model I/O submesh may have its index type and/or geometric primitive type converted to a corresponding Metal type as listed in the tables below. If the geometric primitive type cannot be converted, an error is returned through `error`.

| MDLIndexBitDepth | MTLIndexType |
| --- | --- |
| `MDLIndexBitDepthInvalid` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `MDLIndexBitDepthUInt8` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `MDLIndexBitDepthUInt16` | `MTLIndexTypeUInt16` |
| `MDLIndexBitDepthUInt32` | `MTLIndexTypeUInt32` |

| MDLGeometryType | MTLPrimitiveType |
| --- | --- |
| `MDLGeometryTypePoints` | `MTLPrimitiveTypePoint` |
| `MDLGeometryTypeLines` | `MTLPrimitiveTypeLine` |
| `MDLGeometryTypeTriangleStrips` | `MTLPrimitiveTypeTriangleStrip` |
| `MDLGeometryTypeTriangles` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `MDLGeometryTypeQuads` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `MDLGeometryTypeVariableTopology` | `MTLPrimitiveTypeTriangle` |

> **Note**:  In macOS, vertex buffers allocated from a [`MTKMeshBufferAllocator`](mtkmeshbufferallocator.md) object are aligned to 256 bytes. Index buffers are not aligned.

## Parameters

- `mesh`: The source Model I/O mesh from which to create this MetalKit mesh.
- `device`: The Metal device on which to create MetalKit mesh resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh/init(mesh:device:))*