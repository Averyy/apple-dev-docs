# resolveTexture

**Framework**: Metal  
**Kind**: property

The destination texture used when resolving multisampled texture data into single sample values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var resolveTexture: (any MTLTexture)? { get set }
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)

#### Discussion

If the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) value is set to [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md) or [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md), then the [`resolveTexture`](mtlrenderpassattachmentdescriptor/resolvetexture.md) value must point to a valid texture. Otherwise, Metal ignores this property.

## See Also

- [var resolveLevel: Int](mtlrenderpassattachmentdescriptor/resolvelevel.md)
  The mipmap level of the texture used for the multisample resolve action.
- [var resolveSlice: Int](mtlrenderpassattachmentdescriptor/resolveslice.md)
  The slice of the texture used for the multisample resolve action.
- [var resolveDepthPlane: Int](mtlrenderpassattachmentdescriptor/resolvedepthplane.md)
  The depth plane of the texture used for the multisample resolve action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolvetexture)*