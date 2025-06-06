# MTLStencilOperation.incrementClamp

**Framework**: Metal  
**Kind**: case

If the current stencil value is not the maximum representable value, increase the stencil value by one. Otherwise, if the current stencil value is the maximum representable value, do not change the stencil value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case incrementClamp
```

## See Also

- [MTLStencilOperation.keep](mtlstenciloperation/keep.md)
  Keep the current stencil value.
- [MTLStencilOperation.zero](mtlstenciloperation/zero.md)
  Set the stencil value to zero.
- [MTLStencilOperation.replace](mtlstenciloperation/replace.md)
  Replace the stencil value with the stencil reference value, which is set by the [`setStencilReferenceValue(_:)`](mtlrendercommandencoder/setstencilreferencevalue(_:).md) method of [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md).
- [MTLStencilOperation.decrementClamp](mtlstenciloperation/decrementclamp.md)
  If the current stencil value is not zero, decrease the stencil value by one. Otherwise, if the current stencil value is zero, do not change the stencil value.
- [MTLStencilOperation.invert](mtlstenciloperation/invert.md)
  Perform a logical bitwise invert operation on the current stencil value.
- [MTLStencilOperation.incrementWrap](mtlstenciloperation/incrementwrap.md)
  If the current stencil value is not the maximum representable value, increase the stencil value by one. Otherwise, if the current stencil value is the maximum representable value, set the stencil value to zero.
- [MTLStencilOperation.decrementWrap](mtlstenciloperation/decrementwrap.md)
  If the current stencil value is not zero, decrease the stencil value by one. Otherwise, if the current stencil value is zero, set the stencil value to the maximum representable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstenciloperation/incrementclamp)*