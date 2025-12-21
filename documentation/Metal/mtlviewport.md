# MTLViewport

**Framework**: Metal  
**Kind**: struct

A 3D rectangular region for the viewport clipping.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLViewport
```

## Topics

### Creating a viewport
- [init()](mtlviewport/init.md)
  Returns a new viewport.
- [init(originX: Double, originY: Double, width: Double, height: Double, znear: Double, zfar: Double)](mtlviewport/init(originx:originy:width:height:znear:zfar:).md)
  Returns a new viewport of a specified size at a specified origin.
### Specifying viewport boundaries
- [var originX: Double](mtlviewport/originx.md)
  The x coordinate of the upper-left corner of the viewport.
- [var originY: Double](mtlviewport/originy.md)
  The y coordinate of the upper-left corner of the viewport.
- [var width: Double](mtlviewport/width.md)
  The width of the viewport, in pixels.
- [var height: Double](mtlviewport/height.md)
  The height of the viewport, in pixels.
- [var znear: Double](mtlviewport/znear.md)
  The z coordinate of the near clipping plane of the viewport.
- [var zfar: Double](mtlviewport/zfar.md)
  The z coordinate of the far clipping plane of the viewport.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLScissorRect](mtlscissorrect.md)
  A rectangle for the scissor fragment test.
- [struct MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md)
  An offset applied to a render target index and viewport index.
- [struct MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md)
  The per-patch tessellation factors for a quad patch.
- [struct MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md)
  The per-patch tessellation factors for a triangle patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlviewport)*