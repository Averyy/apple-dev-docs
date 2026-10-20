# resolveDepthPlane

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The depth plane of the texture used for the multisample resolve action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var resolveDepthPlane: Int { get set }
```

```objc
@property (nonatomic) NSUInteger resolveDepthPlane;
```

#### Discussion

If the value of [`storeAction`](./storeaction.md) is set to [`MTLStoreAction.multisampleResolve`](../mtlstoreaction/multisampleresolve.md) or [`MTLStoreAction.storeAndMultisampleResolve`](../mtlstoreaction/storeandmultisampleresolve.md), set this property to point to a depth plane in the resolve texture.

The default value is `0`.

## See Also

### Specifying the texture to resolve multisample data
- [var resolveTexture: (any MTLTexture)?](./resolvetexture.md)
  The destination texture used when resolving multisampled texture data into single sample values.
- [var resolveLevel: Int](./resolvelevel.md)
  The mipmap level of the texture used for the multisample resolve action.
- [var resolveSlice: Int](./resolveslice.md)
  The slice of the texture used for the multisample resolve action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolvedepthplane)*