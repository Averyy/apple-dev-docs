# MTLQuadTessellationFactorsHalf

**Framework**: Metal  
**Kind**: struct

The per-patch tessellation factors for a quad patch.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLQuadTessellationFactorsHalf
```

#### Overview

Refer to the [`Tessellation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Tessellation/Tessellation.html#//apple_ref/doc/uid/TP40014221-CH15) chapter of the [`Metal Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221) for further information.

## Topics

### Initializers
- [init()](mtlquadtessellationfactorshalf/init.md)
  Returns a new per-patch tessellation factors structure.
- [init(edgeTessellationFactor: (UInt16, UInt16, UInt16, UInt16), insideTessellationFactor: (UInt16, UInt16))](mtlquadtessellationfactorshalf/init(edgetessellationfactor:insidetessellationfactor:).md)
  Returns a new per-patch tessellation factors structure with the specified parameters.
### Instance Properties
- [var edgeTessellationFactor: (UInt16, UInt16, UInt16, UInt16)](mtlquadtessellationfactorshalf/edgetessellationfactor.md)
  The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.
- [var insideTessellationFactor: (UInt16, UInt16)](mtlquadtessellationfactorshalf/insidetessellationfactor.md)
  The inside tessellation factors, with the value in index 0 providing the horizontal tessellation factor and the value in index 1 providing the vertical tessellation factor.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLViewport](mtlviewport.md)
  A 3D rectangular region for the viewport clipping.
- [struct MTLScissorRect](mtlscissorrect.md)
  A rectangle for the scissor fragment test.
- [struct MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md)
  An offset applied to a render target index and viewport index.
- [struct MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md)
  The per-patch tessellation factors for a triangle patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf)*