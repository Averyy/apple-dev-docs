# newMeshesFromAsset:device:sourceMeshes:error:

**Framework**: MetalKit  
**Kind**: method  
**Role**: Type Method

Creates and initializes MetalKit meshes from all Model I/O meshes in a Model I/O asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (NSArray<MTKMesh *> *) newMeshesFromAsset:(MDLAsset *) asset device:(id<MTLDevice>) device sourceMeshes:(NSArray<MDLMesh *> **) sourceMeshes error:(NSError **) error;
```

## Return Value

An array of MetalKit mesh objects, or `nil` if an error occured.

## Discussion

This is a convenience method to create MetalKit meshes from each mesh in a source Model I/O asset. The resulting array of [`MTKMesh`](../mtkmesh.md) objects is returned by the method itself, while the [`MDLMesh`](../../ModelIO/mdlmesh.md) objects from which they were generated will be populated into the `sourceMeshes` array provided.

All vertex buffers in each Model I/O asset mesh and the index buffer of each of their submeshes must have been created with a [`MTKMeshBufferAllocator`](../mtkmeshbufferallocator.md) object.

A Model I/O submesh may have its index type and/or geometric primitive type converted to a corresponding Metal type as listed in the tables below. If the geometric primitive type cannot be converted, an error is returned through `error`.

| MDLIndexBitDepth | MTLIndexType |
| --- | --- |
| `MDLIndexBitDepthInvalid` ![](https://developer.apple.com/tutorials/images/com.apple.metalkit/spacer.png) `MDLIndexBitDepthUInt8` ![](https://developer.apple.com/tutorials/images/com.apple.metalkit/spacer.png) `MDLIndexBitDepthUInt16` | `MTLIndexTypeUInt16` |
| `MDLIndexBitDepthUInt32` | `MTLIndexTypeUInt32` |

| MDLGeometryType | MTLPrimitiveType |
| --- | --- |
| `MDLGeometryTypePoints` | `MTLPrimitiveTypePoint` |
| `MDLGeometryTypeLines` | `MTLPrimitiveTypeLine` |
| `MDLGeometryTypeTriangleStrips` | `MTLPrimitiveTypeTriangleStrip` |
| `MDLGeometryTypeTriangles` ![](https://developer.apple.com/tutorials/images/com.apple.metalkit/spacer.png) `MDLGeometryTypeQuads` ![](https://developer.apple.com/tutorials/images/com.apple.metalkit/spacer.png) `MDLGeometryTypeVariableTopology` | `MTLPrimitiveTypeTriangle` |

> **Note**:  In macOS, vertex buffers allocated from a [`MTKMeshBufferAllocator`](../mtkmeshbufferallocator.md) object are aligned to 256 bytes. Index buffers are not aligned.

## Parameters

- `asset`: The source Model I/O asset from which to create MetalKit meshes.
- `device`: The Metal device on which to create MetalKit mesh resources.
- `sourceMeshes`: A pointer to an array of Model I/O meshes that is populated during initialization and corresponds to the returned array of MetalKit meshes. This is an optional parameter and you may pass `nil` to ignore it.
- `error`: A pointer to an [`NSError`](../../Foundation/nserror.md) object if an error occurred, or `nil` if all MetalKit mesh initializations succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh/newmeshesfromasset:device:sourcemeshes:error:)*