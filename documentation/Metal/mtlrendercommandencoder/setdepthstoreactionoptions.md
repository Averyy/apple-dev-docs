# setDepthStoreActionOptions(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action options for the depth attachment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setDepthStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions)
```

## Parameters

- `storeActionOptions`: Additional options for the store action of the depth attachment.

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlrendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Configures the store action options for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlrendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlrendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Configures the store action options for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstoreactionoptions(_:))*