# setDepthStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action for the depth attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setDepthStoreAction(_ storeAction: MTLStoreAction)
```

#### Discussion

This method changes the render command encoder’s store action for the depth attachment. You can assign the default store action for the depth attachment by configuring the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property of its [`MTLRenderPassDepthAttachmentDescriptor`](mtlrenderpassdepthattachmentdescriptor.md) (see [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) and its [`depthAttachment`](mtlrenderpassdescriptor/depthattachment.md) property).

> ❗ **Important**:  You need to call this method before calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method, but only if the depth attachment’s [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property is equal to [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md).

 You need to call this method before calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method, but only if the depth attachment’s [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property is equal to [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md).

## Parameters

- `storeAction`: A store action for the depth attachment that can’t be  .

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlrendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Configures the store action options for a color attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Configures the store action options for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlrendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Configures the store action options for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstoreaction(_:))*