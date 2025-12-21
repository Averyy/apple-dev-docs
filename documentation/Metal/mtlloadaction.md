# MTLLoadAction

**Framework**: Metal  
**Kind**: enum

Types of actions performed for an attachment at the start of a rendering pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLLoadAction
```

## Mentions

- [Setting load and store actions](setting-load-and-store-actions.md)

## Topics

### Load actions
- [MTLLoadAction.dontCare](mtlloadaction/dontcare.md)
  The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.
- [MTLLoadAction.load](mtlloadaction/load.md)
  The GPU preserves the existing contents of the attachment at the start of the render pass.
- [MTLLoadAction.clear](mtlloadaction/clear.md)
  The GPU writes a value to every pixel in the attachment at the start of the render pass.
### Initializers
- [init?(rawValue: UInt)](mtlloadaction/init(rawvalue:).md)

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
  An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [enum MTLStoreAction](mtlstoreaction.md)
  Types of actions performed for an attachment at the end of a rendering pass.
- [struct MTLStoreActionOptions](mtlstoreactionoptions.md)
  Options that modify a store action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlloadaction)*