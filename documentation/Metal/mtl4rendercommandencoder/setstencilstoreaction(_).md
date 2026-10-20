# setStencilStoreAction(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setStencilStoreAction:(MTLStoreAction) storeAction;
```

## Parameters

- `storeAction`: A store action for the stencil attachment that can’t be [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](./setcolorstoreaction%28_,index%29.md)
  Configures the store action for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](./setdepthstoreaction%28_%29.md)
  Configures the store action for the depth attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilstoreaction(_:))*