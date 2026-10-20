# setDepthStoreActionOptions(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Specifies known store action options for a given depth attachment.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Store action options have no effect on Apple Silicon

## Declaration

```swift
func setDepthStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions)
```

```objc
- (void) setDepthStoreActionOptions:(MTLStoreActionOptions) storeActionOptions;
```

## Parameters

- `storeActionOptions`: The additional store action options for the depth attachment.

## See Also

### Setting render pass state
- [func setColorStoreAction(MTLStoreAction, index: Int)](./setcolorstoreaction%28_,index%29.md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](./setcolorstoreactionoptions%28_,index%29.md)
  Specifies known store action options for a given color attachment.
- [func setDepthStoreAction(MTLStoreAction)](./setdepthstoreaction%28_%29.md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](./setstencilstoreaction%28_%29.md)
  Specifies a known store action to replace the initial [`MTLStoreAction.unknown`](../mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](./setstencilstoreactionoptions%28_%29.md)
  Specifies known store action options for a given stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setdepthstoreactionoptions(_:))*