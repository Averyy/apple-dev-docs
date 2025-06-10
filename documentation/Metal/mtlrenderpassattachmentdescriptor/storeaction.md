# storeAction

**Framework**: Metal  
**Kind**: property

The action performed by this attachment at the end of a rendering pass for a render command encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var storeAction: MTLStoreAction { get set }
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)
- [Storing Data a Pass Makes with Custom Sample Positions for a Subsequent Pass](storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

#### Discussion

If your app doesn’t need the data in the texture after completing the rendering pass, use the [`MTLStoreAction.dontCare`](mtlstoreaction/dontcare.md) action. Otherwise, use the [`MTLStoreAction.store`](mtlstoreaction/store.md) action if the texture is directly stored or the [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md) action if the texture is a multisampled texture. In some feature sets, you can use the [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md) action to store and resolve the texture in a single rendering pass. For more information, see:

- [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [`Metal feature set tables (Numbers)`](https://developer.apple.comhttps://developer.apple.com/metal/metal-feature-set-tables.zip)

When the store action is either [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md) or [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md), the [`resolveTexture`](mtlrenderpassattachmentdescriptor/resolvetexture.md) property must be set to the texture to use as the target for the resolve action. Use the [`resolveLevel`](mtlrenderpassattachmentdescriptor/resolvelevel.md), [`resolveSlice`](mtlrenderpassattachmentdescriptor/resolveslice.md), and [`resolveDepthPlane`](mtlrenderpassattachmentdescriptor/resolvedepthplane.md) properties to specify the mipmap level, cube slice, and depth plane of the resolve texture, respectively.

For color render targets, the default value is [`MTLStoreAction.store`](mtlstoreaction/store.md). For depth or stencil render targets, the default value is [`MTLStoreAction.dontCare`](mtlstoreaction/dontcare.md).

## See Also

- [var loadAction: MTLLoadAction](mtlrenderpassattachmentdescriptor/loadaction.md)
  The action performed by this attachment at the start of a rendering pass for a render command encoder.
- [var storeActionOptions: MTLStoreActionOptions](mtlrenderpassattachmentdescriptor/storeactionoptions.md)
  The options that modify the store action performed by this attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/storeaction)*