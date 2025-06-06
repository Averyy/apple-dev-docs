# MTLStoreAction.unknown

**Framework**: Metal  
**Kind**: case

The system selects a store action when it encodes the render pass.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case unknown
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)

#### Discussion

Only apply this action if you can’t determine the store action when you create the render pass descriptor. You must specify a store action before you finish encoding commands into the render command encoder. Refer to the [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) and [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) protocol references for further information.

## See Also

- [MTLStoreAction.dontCare](mtlstoreaction/dontcare.md)
  The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreAction.store](mtlstoreaction/store.md)
  The GPU stores the rendered contents to the texture.
- [MTLStoreAction.multisampleResolve](mtlstoreaction/multisampleresolve.md)
  The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreAction.storeAndMultisampleResolve](mtlstoreaction/storeandmultisampleresolve.md)
  The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreAction.customSampleDepthStore](mtlstoreaction/customsampledepthstore.md)
  The GPU stores depth data in a sample-position–agnostic representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreaction/unknown)*