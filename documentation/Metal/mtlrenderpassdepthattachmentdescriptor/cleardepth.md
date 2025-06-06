# clearDepth

**Framework**: Metal  
**Kind**: property

The depth to use when clearing the depth attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var clearDepth: Double { get set }
```

#### Discussion

If the [`loadAction`](mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [`MTLLoadAction.clear`](mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the contents of the attachment with the value stored in the [`clearDepth`](mtlrenderpassdepthattachmentdescriptor/cleardepth.md) property. Otherwise, the GPU ignores [`clearDepth`](mtlrenderpassdepthattachmentdescriptor/cleardepth.md).

The default value is `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/cleardepth)*