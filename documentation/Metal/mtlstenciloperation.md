# MTLStencilOperation

**Framework**: Metal  
**Kind**: enum

The operation performed on a currently stored stencil value when a comparison test passes or fails.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLStencilOperation
```

## Topics

### Stencil operations
- [MTLStencilOperation.keep](mtlstenciloperation/keep.md)
  A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperation.zero](mtlstenciloperation/zero.md)
  A stencil operation that sets a stencil value to zero.
- [MTLStencilOperation.replace](mtlstenciloperation/replace.md)
  A stencil operation that replaces a stencil value with a reference value.
- [MTLStencilOperation.incrementClamp](mtlstenciloperation/incrementclamp.md)
  A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperation.decrementClamp](mtlstenciloperation/decrementclamp.md)
  A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperation.invert](mtlstenciloperation/invert.md)
  A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperation.incrementWrap](mtlstenciloperation/incrementwrap.md)
  A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperation.decrementWrap](mtlstenciloperation/decrementwrap.md)
  A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.
### Initializers
- [init?(rawValue: UInt)](mtlstenciloperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var stencilFailureOperation: MTLStencilOperation](mtlstencildescriptor/stencilfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [var depthFailureOperation: MTLStencilOperation](mtlstencildescriptor/depthfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [var depthStencilPassOperation: MTLStencilOperation](mtlstencildescriptor/depthstencilpassoperation.md)
  The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [var stencilCompareFunction: MTLCompareFunction](mtlstencildescriptor/stencilcomparefunction.md)
  The comparison that is performed between the masked reference value and a masked value in the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstenciloperation)*