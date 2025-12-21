# MTLScissorRect

**Framework**: Metal  
**Kind**: struct

A rectangle for the scissor fragment test.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLScissorRect
```

## Topics

### Creating a scissor rectangle
- [init()](mtlscissorrect/init.md)
- [init(x: Int, y: Int, width: Int, height: Int)](mtlscissorrect/init(x:y:width:height:).md)
### Specifying scissor boundaries
- [var height: Int](mtlscissorrect/height.md)
  The height of the scissor rectangle, in pixels.
- [var width: Int](mtlscissorrect/width.md)
  The width of the scissor rectangle, in pixels.
- [var x: Int](mtlscissorrect/x.md)
  The x window coordinate of the upper-left corner of the scissor rectangle.
- [var y: Int](mtlscissorrect/y.md)
  The y window coordinate of the upper-left corner of the scissor rectangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLViewport](mtlviewport.md)
  A 3D rectangular region for the viewport clipping.
- [struct MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md)
  An offset applied to a render target index and viewport index.
- [struct MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md)
  The per-patch tessellation factors for a quad patch.
- [struct MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md)
  The per-patch tessellation factors for a triangle patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlscissorrect)*