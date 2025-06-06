# MTLVertexAmplificationViewMapping

**Framework**: Metal  
**Kind**: struct

An offset applied to a render target index and viewport index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLVertexAmplificationViewMapping
```

## Mentions

- [Improving Rendering Performance with Vertex Amplification](improving-rendering-performance-with-vertex-amplification.md)

## Topics

### Creating a View Mapping
- [init()](mtlvertexamplificationviewmapping/init.md)
  Initializes a default view mapping.
- [init(viewportArrayIndexOffset: UInt32, renderTargetArrayIndexOffset: UInt32)](mtlvertexamplificationviewmapping/init(viewportarrayindexoffset:rendertargetarrayindexoffset:).md)
  Initializes a new view mapping.
### Specifying Mapping Offsets
- [var renderTargetArrayIndexOffset: UInt32](mtlvertexamplificationviewmapping/rendertargetarrayindexoffset.md)
  An offset into the list of render targets.
- [var viewportArrayIndexOffset: UInt32](mtlvertexamplificationviewmapping/viewportarrayindexoffset.md)
  An offset into the list of viewports.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLViewport](mtlviewport.md)
  A 3D rectangular region for the viewport clipping.
- [struct MTLScissorRect](mtlscissorrect.md)
  A rectangle for the scissor fragment test.
- [struct MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md)
  The per-patch tessellation factors for a quad patch.
- [struct MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md)
  The per-patch tessellation factors for a triangle patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexamplificationviewmapping)*