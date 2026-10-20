# setColorStoreAction(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given color attachment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setColorStoreAction(_ storeAction: MTLStoreAction, index colorAttachmentIndex: Int)
```

```objc
- (void) setColorStoreAction:(MTLStoreAction) storeAction atIndex:(NSUInteger) colorAttachmentIndex;
```

#### Discussion

If the store action for the given color attachment was set to [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) when the parallel render command encoder was created, you need to call this method to specify another store action before you call the [`endEncoding()`](../mtlcommandencoder/endencoding%28%29.md) method.

## Parameters

- `storeAction`: The desired store action for the color attachment. This value can’t be [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md).
- `colorAttachmentIndex`: The index of the color attachment.

## See Also

### Setting render pass state
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](./setcolorstoreactionoptions%28_,index%29.md)
  Specifies known store action options for a given color attachment.
- [func setDepthStoreAction(MTLStoreAction)](./setdepthstoreaction%28_%29.md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](./setdepthstoreactionoptions%28_%29.md)
  Specifies known store action options for a given depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](./setstencilstoreactionoptions%28_%29.md)
  Specifies known store action options for a given stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreaction(_:index:))*