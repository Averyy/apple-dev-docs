# setColorStoreActionOptions(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures the store action options for a color attachment.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Store action options have no effect on Apple Silicon

## Declaration

```swift
func setColorStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions, index colorAttachmentIndex: Int)
```

```objc
- (void) setColorStoreActionOptions:(MTLStoreActionOptions) storeActionOptions atIndex:(NSUInteger) colorAttachmentIndex;
```

## Parameters

- `storeActionOptions`: Additional options for the store action of a color attachment.
- `colorAttachmentIndex`: The index of a color attachment.

## See Also

### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](./setcolorstoreaction%28_,index%29.md)
  Configures the store action for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](./setdepthstoreaction%28_%29.md)
  Configures the store action for the depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](./setdepthstoreactionoptions%28_%29.md)
  Configures the store action options for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](./setstencilstoreactionoptions%28_%29.md)
  Configures the store action options for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcolorstoreactionoptions(_:index:))*