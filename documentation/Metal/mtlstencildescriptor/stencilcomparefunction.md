# stencilCompareFunction

**Framework**: Metal  
**Kind**: property

The comparison that is performed between the masked reference value and a masked value in the stencil attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stencilCompareFunction: MTLCompareFunction { get set }
```

#### Discussion

For example, if `stencilCompareFunction` is [`MTLCompareFunction.less`](mtlcomparefunction/less.md), then the stencil test passes if the masked reference value is less than the masked stored stencil value. The default value is [`MTLCompareFunction.always`](mtlcomparefunction/always.md), which indicates that the stencil test always passes.

The stored stencil value and the reference value are both  by performing a logical AND operation with the [`readMask`](mtlstencildescriptor/readmask.md) value before the comparison takes place. For more information on possible values, see [`MTLCompareFunction`](mtlcomparefunction.md).

## See Also

- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [var stencilFailureOperation: MTLStencilOperation](mtlstencildescriptor/stencilfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [var depthFailureOperation: MTLStencilOperation](mtlstencildescriptor/depthfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [var depthStencilPassOperation: MTLStencilOperation](mtlstencildescriptor/depthstencilpassoperation.md)
  The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [enum MTLStencilOperation](mtlstenciloperation.md)
  The operation performed on a currently stored stencil value when a comparison test passes or fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor/stencilcomparefunction)*