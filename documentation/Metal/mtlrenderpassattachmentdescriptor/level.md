# level

**Framework**: Metal  
**Kind**: property

The mipmap level of the texture used for rendering to the attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var level: Int { get set }
```

#### Discussion

The default value is `0`.

## See Also

- [var texture: (any MTLTexture)?](mtlrenderpassattachmentdescriptor/texture.md)
  The texture object associated with this attachment.
- [var slice: Int](mtlrenderpassattachmentdescriptor/slice.md)
  The slice of the texture used for rendering to the attachment.
- [var depthPlane: Int](mtlrenderpassattachmentdescriptor/depthplane.md)
  The depth plane of the texture used for rendering to the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/level)*