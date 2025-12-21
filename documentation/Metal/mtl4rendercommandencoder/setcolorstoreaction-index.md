# setColorStoreAction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the store action for a color attachment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setColorStoreAction(_ storeAction: MTLStoreAction, index colorAttachmentIndex: Int)
```

## Parameters

- `storeAction`: A store action for the color attachment that   can’t be  .
- `colorAttachmentIndex`: The index of a color attachment.

## See Also

- [func setDepthStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcolorstoreaction(_:index:))*