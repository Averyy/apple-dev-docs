# setColorStoreActionOptions(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Specifies known store action options for a given color attachment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setColorStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions, index colorAttachmentIndex: Int)
```

## Parameters

- `storeActionOptions`: The additional store action options for the color attachment.
- `colorAttachmentIndex`: The index of the color attachment.

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlparallelrendercommandencoder/setcolorstoreaction(_:index:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlparallelrendercommandencoder/setdepthstoreaction(_:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Specifies known store action options for a given depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlparallelrendercommandencoder/setstencilstoreaction(_:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Specifies known store action options for a given stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreactionoptions(_:index:))*