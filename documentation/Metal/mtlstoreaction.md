# MTLStoreAction

**Framework**: Metal  
**Kind**: enum

Types of actions performed for an attachment at the end of a rendering pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLStoreAction
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)

## Topics

### Constants
- [MTLStoreAction.dontCare](mtlstoreaction/dontcare.md)
  The GPU has permission to discard the rendered contents of the attachment at the end of the render pass, replacing them with arbitrary data.
- [MTLStoreAction.store](mtlstoreaction/store.md)
  The GPU stores the rendered contents to the texture.
- [MTLStoreAction.multisampleResolve](mtlstoreaction/multisampleresolve.md)
  The GPU resolves the multisampled data to one sample per pixel and stores the data to the resolve texture, discarding the multisample data afterwards.
- [MTLStoreAction.storeAndMultisampleResolve](mtlstoreaction/storeandmultisampleresolve.md)
  The GPU stores the multisample data to the multisample texture, resolves the data to a sample per pixel, and stores the data to the resolve texture.
- [MTLStoreAction.unknown](mtlstoreaction/unknown.md)
  The system selects a store action when it encodes the render pass.
- [MTLStoreAction.customSampleDepthStore](mtlstoreaction/customsampledepthstore.md)
  The GPU stores depth data in a sample-position–agnostic representation.
### Initializers
- [init?(rawValue: UInt)](mtlstoreaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md)
  An object that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [enum MTLLoadAction](mtlloadaction.md)
  Types of actions performed for an attachment at the start of a rendering pass.
- [struct MTLStoreActionOptions](mtlstoreactionoptions.md)
  Options that modify a store action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreaction)*