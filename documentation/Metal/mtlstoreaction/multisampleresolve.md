# MTLStoreAction.multisampleResolve

**Framework**: Metal  
**Kind**: case

The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case multisampleResolve
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)

#### Discussion

Use this option when you need to resolve the multisample attachment’s contents at the end of the render pass but don’t need the multisample data afterwards. Some GPUs may still store the multisample data back to the texture, but you can’t rely on that behavior. You must assume that GPU discarded the multisample texture’s contents.

## See Also

- [MTLStoreAction.dontCare](mtlstoreaction/dontcare.md)
  The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreAction.store](mtlstoreaction/store.md)
  The GPU stores the rendered contents to the texture.
- [MTLStoreAction.storeAndMultisampleResolve](mtlstoreaction/storeandmultisampleresolve.md)
  The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreAction.unknown](mtlstoreaction/unknown.md)
  The system selects a store action when it encodes the render pass.
- [MTLStoreAction.customSampleDepthStore](mtlstoreaction/customsampledepthstore.md)
  The GPU stores depth data in a sample-position–agnostic representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreaction/multisampleresolve)*