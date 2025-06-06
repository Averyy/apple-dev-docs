# setStencilStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given stencil attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setStencilStoreAction(_ storeAction: MTLStoreAction)
```

#### Discussion

If the store action for the given stencil attachment was set to [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) when the parallel render command encoder was created, you must call this method to specify another store action before you call the [`endEncoding()`](mtlcommandencoder/endencoding().md) method.

## Parameters

- `storeAction`: The desired store action for the stencil attachment. This value must not be  .

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlparallelrendercommandencoder/setcolorstoreaction(_:index:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlparallelrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Specifies known store action options for a given color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlparallelrendercommandencoder/setdepthstoreaction(_:).md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Specifies known store action options for a given depth attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlparallelrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Specifies known store action options for a given stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setstencilstoreaction(_:))*