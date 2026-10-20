# setDepthStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setDepthStoreAction:(MTLStoreAction) storeAction;
```

## Parameters

- `storeAction`: A store action for the depth attachment that can’t be [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](./setcolorstoreaction%28_,index%29.md)
  Configures the store action for a color attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Configures the store action for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthstoreaction(_:))*