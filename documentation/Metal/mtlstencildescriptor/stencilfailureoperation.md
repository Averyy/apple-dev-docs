# stencilFailureOperation

**Framework**: Metal  
**Kind**: property

The operation that is performed to update the values in the stencil attachment when the stencil test fails.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stencilFailureOperation: MTLStencilOperation { get set }
```

#### Discussion

The default value is [`MTLStencilOperation.keep`](mtlstenciloperation/keep.md), which does not change the current stencil value. For more information on possible values, see [`MTLStencilOperation`](mtlstenciloperation.md).

When the stencil test fails for a pixel, its incoming color, depth, or stencil values are discarded.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var depthFailureOperation: MTLStencilOperation](mtlstencildescriptor/depthfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [var depthStencilPassOperation: MTLStencilOperation](mtlstencildescriptor/depthstencilpassoperation.md)
  The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [var stencilCompareFunction: MTLCompareFunction](mtlstencildescriptor/stencilcomparefunction.md)
  The comparison that is performed between the masked reference value and a masked value in the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/stencilfailureoperation)*