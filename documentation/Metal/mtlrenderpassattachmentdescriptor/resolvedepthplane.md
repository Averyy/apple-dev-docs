# resolveDepthPlane

**Framework**: Metal  
**Kind**: property

The depth plane of the texture used for the multisample resolve action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var resolveDepthPlane: Int { get set }
```

#### Discussion

If the value of [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) is set to [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md) or [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md), set this property to point to a depth plane in the resolve texture.

The default value is `0`.

## See Also

- [var resolveTexture: (any MTLTexture)?](mtlrenderpassattachmentdescriptor/resolvetexture.md)
  The destination texture used when resolving multisampled texture data into single sample values.
- [var resolveLevel: Int](mtlrenderpassattachmentdescriptor/resolvelevel.md)
  The mipmap level of the texture used for the multisample resolve action.
- [var resolveSlice: Int](mtlrenderpassattachmentdescriptor/resolveslice.md)
  The slice of the texture used for the multisample resolve action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolvedepthplane)*