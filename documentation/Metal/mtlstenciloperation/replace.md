# MTLStencilOperation.replace

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A stencil operation that replaces a stencil value with a reference value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case replace
```

```c
MTLStencilOperationReplace
```

## Discussion

You can set by the reference value by calling the [`setStencilReferenceValue(_:)`](../mtlrendercommandencoder/setstencilreferencevalue%28_%29.md) method of an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance.

## See Also

### Stencil operations
- [MTLStencilOperation.keep](./keep.md)
  A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperation.zero](./zero.md)
  A stencil operation that sets a stencil value to zero.
- [MTLStencilOperation.incrementClamp](./incrementclamp.md)
  A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperation.decrementClamp](./decrementclamp.md)
  A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperation.invert](./invert.md)
  A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperation.incrementWrap](./incrementwrap.md)
  A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperation.decrementWrap](./decrementwrap.md)
  A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstenciloperation/replace)*