# MTLStoreAction.store

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The GPU stores the rendered contents to the texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case store
```

```c
MTLStoreActionStore
```

## Mentions

- [Setting load and store actions](../setting-load-and-store-actions.md)
- [Storing data a pass makes with custom sample positions for a subsequent pass](../storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

## See Also

### Store actions
- [MTLStoreAction.dontCare](./dontcare.md)
  The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreAction.multisampleResolve](./multisampleresolve.md)
  The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreAction.storeAndMultisampleResolve](./storeandmultisampleresolve.md)
  The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreAction.unknown](./unknown.md)
  The system selects a store action when it encodes the render pass.
- [MTLStoreAction.customSampleDepthStore](./customsampledepthstore.md)
  The GPU stores depth data in a sample-position–agnostic representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreaction/store)*