# depthFailureOperation

**Framework**: Metal  
**Kind**: property

The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var depthFailureOperation: MTLStencilOperation { get set }
```

#### Discussion

The default value is [`MTLStencilOperation.keep`](mtlstenciloperation/keep.md), which does not change the current stencil value. For more information on possible values, see [`MTLStencilOperation`](mtlstenciloperation.md).

## See Also

- [var depthCompareFunction: MTLCompareFunction](mtldepthstencildescriptor/depthcomparefunction.md)
  The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.
- [var stencilFailureOperation: MTLStencilOperation](mtlstencildescriptor/stencilfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [var depthStencilPassOperation: MTLStencilOperation](mtlstencildescriptor/depthstencilpassoperation.md)
  The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [var stencilCompareFunction: MTLCompareFunction](mtlstencildescriptor/stencilcomparefunction.md)
  The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
- [enum MTLStencilOperation](mtlstenciloperation.md)
  The operation performed on a currently stored stencil value when a comparison test passes or fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/depthfailureoperation)*