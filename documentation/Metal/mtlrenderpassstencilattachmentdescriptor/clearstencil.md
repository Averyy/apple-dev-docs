# clearStencil

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The value to use when clearing the stencil attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearStencil: UInt32 { get set }
```

```objc
@property (nonatomic) uint32_t clearStencil;
```

## Discussion

If the [`loadAction`](../mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [`MTLLoadAction.clear`](../mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the contents of the attachment with the value stored in the [`clearStencil`](./clearstencil.md) property. Otherwise, the GPU ignores [`clearStencil`](./clearstencil.md).

The default value is `0`.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor/clearstencil)*