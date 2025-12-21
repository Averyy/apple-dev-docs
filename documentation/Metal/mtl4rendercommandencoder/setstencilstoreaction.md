# setStencilStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action for the stencil attachment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setStencilStoreAction(_ storeAction: MTLStoreAction)
```

## Parameters

- `storeAction`: A store action for the stencil attachment that   can’t be  .

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtl4rendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilstoreaction(_:))*