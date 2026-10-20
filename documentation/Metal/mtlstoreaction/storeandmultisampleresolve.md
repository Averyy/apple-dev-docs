# MTLStoreAction.storeAndMultisampleResolve

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case storeAndMultisampleResolve
```

```c
MTLStoreActionStoreAndMultisampleResolve
```

## Mentions

- [Setting load and store actions](../setting-load-and-store-actions.md)

## See Also

### Store actions
- [MTLStoreAction.dontCare](./dontcare.md)
  The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreAction.store](./store.md)
  The GPU stores the rendered contents to the texture.
- [MTLStoreAction.multisampleResolve](./multisampleresolve.md)
  The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreAction.unknown](./unknown.md)
  The system selects a store action when it encodes the render pass.
- [MTLStoreAction.customSampleDepthStore](./customsampledepthstore.md)
  The GPU stores depth data in a sample-position–agnostic representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve)*