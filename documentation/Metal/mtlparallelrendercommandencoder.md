# MTLParallelRenderCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An object that splits up a single render pass so that it can be simultaneously encoded from multiple threads.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Your app does not define classes that implement this protocol. To create a [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) object, call the [`makeParallelRenderCommandEncoder(descriptor:)`](mtlcommandbuffer/makeparallelrendercommandencoder(descriptor:).md) method of the [`MTLCommandBuffer`](mtlcommandbuffer.md) object that you want to encode the rendering commands into. Then, call the renderCommandEncoder method on this [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) object to create one or more [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) objects. The subordinate [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) objects created encode their commands to the same command buffer and target the same [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) object. The [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) object ensures the attachment load and store actions only occur at the start and end of the entire rendering pass.

You can assign each [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) to its own thread and each can encode commands in parallel. You are responsible for any thread synchronization that is required. After all the subordinate encoders have finished encoding their commands, call [`endEncoding()`](mtlcommandencoder/endencoding().md) to execute the commands. The rendering commands are executed in the order that the subordinate encoders were created.

## Topics

### Creating a Render Command Encoder
- [func makeRenderCommandEncoder() -> (any MTLRenderCommandEncoder)?](mtlparallelrendercommandencoder/makerendercommandencoder.md)
  Create an object that encodes commands that perform graphics rendering operations and may be assigned to a different thread.
### Setting Render Pass State
- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlparallelrendercommandencoder/setcolorstoreaction(_:index:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlparallelrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Specifies known store action options for a given color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlparallelrendercommandencoder/setdepthstoreaction(_:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Specifies known store action options for a given depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlparallelrendercommandencoder/setstencilstoreaction(_:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Specifies known store action options for a given stencil attachment.

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum MTLLoadAction](mtlloadaction.md)
  Types of actions performed for an attachment at the start of a rendering pass.
- [enum MTLStoreAction](mtlstoreaction.md)
  Types of actions performed for an attachment at the end of a rendering pass.
- [struct MTLStoreActionOptions](mtlstoreactionoptions.md)
  Options that modify a store action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder)*