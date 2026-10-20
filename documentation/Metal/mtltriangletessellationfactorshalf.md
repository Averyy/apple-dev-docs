# MTLTriangleTessellationFactorsHalf

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The per-patch tessellation factors for a triangle patch.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLTriangleTessellationFactorsHalf
```

```c
typedef struct { ... } MTLTriangleTessellationFactorsHalf;
```

#### Overview

Refer to the [Tessellation](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Tessellation/Tessellation.html#//apple_ref/doc/uid/TP40014221-CH15) chapter of the [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221) for further information.

## Topics

### Initializers
- [init()](./mtltriangletessellationfactorshalf/init%28%29.md)
- [init(edgeTessellationFactor: (UInt16, UInt16, UInt16), insideTessellationFactor: UInt16)](./mtltriangletessellationfactorshalf/init%28edgetessellationfactor,insidetessellationfactor%29.md)
### Instance Properties
- [var edgeTessellationFactor: (UInt16, UInt16, UInt16)](./mtltriangletessellationfactorshalf/edgetessellationfactor.md)
  The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.
- [var insideTessellationFactor: UInt16](./mtltriangletessellationfactorshalf/insidetessellationfactor.md)
  The inside tessellation factor.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Dynamic render pipeline states
- [struct MTLViewport](./mtlviewport.md)
  A 3D rectangular region for the viewport clipping.
- [struct MTLScissorRect](./mtlscissorrect.md)
  A rectangle for the scissor fragment test.
- [struct MTLVertexAmplificationViewMapping](./mtlvertexamplificationviewmapping.md)
  An offset applied to a render target index and viewport index.
- [struct MTLQuadTessellationFactorsHalf](./mtlquadtessellationfactorshalf.md)
  The per-patch tessellation factors for a quad patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf)*