# setColorStoreAction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action for a color attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setColorStoreAction(_ storeAction: MTLStoreAction, index colorAttachmentIndex: Int)
```

#### Discussion

This method changes the render command encoder’s store action for a color attachment. You can assign the default store action for a color attachment by configuring the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property of its [`MTLRenderPassColorAttachmentDescriptor`](mtlrenderpasscolorattachmentdescriptor.md) (see [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) and its [`colorAttachments`](mtlrenderpassdescriptor/colorattachments.md) property).

> ❗ **Important**:  You need to call this method before calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method, but only for color attachments with a [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property equal to [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md).

 You need to call this method before calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method, but only for color attachments with a [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property equal to [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md).

## Parameters

- `storeAction`: A store action for the color attachment that can’t be  .
- `colorAttachmentIndex`: The index of a color attachment.

## See Also

- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Configures the store action options for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlrendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Configures the store action options for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlrendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Configures the store action options for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcolorstoreaction(_:index:))*