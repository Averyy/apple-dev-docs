# setColorStoreAction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setColorStoreAction:(MTLStoreAction) storeAction atIndex:(NSUInteger) colorAttachmentIndex;
```

## Parameters

- `storeAction`: A store action for the color attachment that can’t be [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).
- `colorAttachmentIndex`: The index of a color attachment.

## See Also

### Configuring the actions for attachments
- [func setDepthStoreAction(MTLStoreAction)](./setdepthstoreaction%28_%29.md)
  Configures the store action for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Configures the store action for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcolorstoreaction(_:index:))*