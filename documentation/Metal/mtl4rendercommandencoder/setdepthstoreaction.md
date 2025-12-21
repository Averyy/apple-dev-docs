# setDepthStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action for the depth attachment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setDepthStoreAction(_ storeAction: MTLStoreAction)
```

## Parameters

- `storeAction`: A store action for the depth attachment that   can’t be  .

## See Also

- [func setColorStoreAction(MTLStoreAction, index: Int)](mtl4rendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthstoreaction(_:))*