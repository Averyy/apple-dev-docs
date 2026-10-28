# depthStencilPassOperation

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var depthStencilPassOperation: MTLStencilOperation { get set }
```

```objc
@property (nonatomic) MTLStencilOperation depthStencilPassOperation;
```

## Discussion

The default value is [`MTLStencilOperation.keep`](../mtlstenciloperation/keep.md), which does not change the current stencil value. For more information on possible values, see [`MTLStencilOperation`](../mtlstenciloperation.md).

## See Also

### Related Documentation
- [var depthCompareFunction: MTLCompareFunction](../mtldepthstencildescriptor/depthcomparefunction.md)
  The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.
### Configuring stencil functions and operations
- [var stencilFailureOperation: MTLStencilOperation](./stencilfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [var depthFailureOperation: MTLStencilOperation](./depthfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [var stencilCompareFunction: MTLCompareFunction](./stencilcomparefunction.md)
  The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
- [enum MTLStencilOperation](../mtlstenciloperation.md)
  The operation performed on a currently stored stencil value when a comparison test passes or fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/depthstencilpassoperation)*