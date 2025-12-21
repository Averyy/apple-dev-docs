# MTLStencilOperation.zero

**Framework**: Metal  
**Kind**: case

A stencil operation that sets a stencil value to zero.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case zero
```

## See Also

- [MTLStencilOperation.keep](mtlstenciloperation/keep.md)
  A stencil operation that doesn’t modify a stencil value.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstenciloperation/zero)*