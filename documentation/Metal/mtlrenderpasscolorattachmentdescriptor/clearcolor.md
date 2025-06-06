# clearColor

**Framework**: Metal  
**Kind**: property

The color to use when clearing the color attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var clearColor: MTLClearColor { get set }
```

#### Discussion

If the [`loadAction`](mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [`MTLLoadAction.clear`](mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the texture with the value stored in the [`clearColor`](mtlrenderpasscolorattachmentdescriptor/clearcolor.md) property. Otherwise, the GPU ignores the [`clearColor`](mtlrenderpasscolorattachmentdescriptor/clearcolor.md) property.

The [`clearColor`](mtlrenderpasscolorattachmentdescriptor/clearcolor.md) property represents a set of RGBA components. The default value is `(0.0, 0.0, 0.0, 1.0)` (black). Use the [`MTLClearColorMake(_:_:_:_:)`](mtlclearcolormake(_:_:_:_:).md) function to construct a [`MTLClearColor`](mtlclearcolor.md) value.

## See Also

- [func MTLClearColorMake(Double, Double, Double, Double) -> MTLClearColor](mtlclearcolormake(_:_:_:_:).md)
  Returns a color value used to clear a color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor/clearcolor)*