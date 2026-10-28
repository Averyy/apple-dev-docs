# setDepthStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setDepthStoreAction:(MTLStoreAction) storeAction;
```

## Discussion

This method changes the render command encoder’s store action for the depth attachment. You can assign the default store action for the depth attachment by configuring the [`storeAction`](../mtlrenderpassattachmentdescriptor/storeaction.md) property of its [`MTLRenderPassDepthAttachmentDescriptor`](../mtlrenderpassdepthattachmentdescriptor.md) (see [`MTLRenderPassDescriptor`](../mtlrenderpassdescriptor.md) and its [`depthAttachment`](../mtlrenderpassdescriptor/depthattachment.md) property).

> ❗ **Important**:  You need to call this method before calling the encoder’s [`endEncoding()`](../mtlcommandencoder/endencoding%28%29.md) method, but only if the depth attachment’s [`storeAction`](../mtlrenderpassattachmentdescriptor/storeaction.md) property is equal to [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).

## Parameters

- `storeAction`: A store action for the depth attachment that can’t be [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](./setcolorstoreaction%28_,index%29.md)
  Configures the store action for a color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](./setcolorstoreactionoptions%28_,index%29.md)
  Configures the store action options for a color attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](./setdepthstoreactionoptions%28_%29.md)
  Configures the store action options for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](./setstencilstoreactionoptions%28_%29.md)
  Configures the store action options for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstoreaction(_:))*