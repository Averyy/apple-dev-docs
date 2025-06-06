# customSamplePositions

**Framework**: Metal  
**Kind**: property

An option that stores data in a sample-position–agnostic representation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var customSamplePositions: MTLStoreActionOptions { get }
```

## Mentions

- [Storing Data a Pass Makes with Custom Sample Positions for a Subsequent Pass](storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

#### Discussion

Set this option only on a [`MTLRenderPassColorAttachmentDescriptor`](mtlrenderpasscolorattachmentdescriptor.md) or [`MTLRenderPassDepthAttachmentDescriptor`](mtlrenderpassdepthattachmentdescriptor.md) object. Setting this option on a [`MTLRenderPassStencilAttachmentDescriptor`](mtlrenderpassstencilattachmentdescriptor.md) object or combining it with a nonstore [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) value results in a runtime error.

Set this action when you need to read the data in a subsequent render pass or blit operation that is unaware of the programmable sample positions used to generate the data. You should set this option when, for example, reading per-sample data within a fragment function that uses different programmable sample positions.

If you specify this action, Metal may decompress the depth render target and store the resulting data in its decompressed form. If you don’t change programmable sample positions in a subsequent render pass, use [`MTLStoreAction.store`](mtlstoreaction/store.md) instead to improve performance.

## See Also

- [init(rawValue: UInt)](mtlstoreactionoptions/init(rawvalue:).md)
  Creates a store action option from a raw integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreactionoptions/customsamplepositions)*