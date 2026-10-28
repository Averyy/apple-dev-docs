# depthPlane

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The depth plane of the texture used for rendering to the attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var depthPlane: Int { get set }
```

```objc
@property (nonatomic) NSUInteger depthPlane;
```

## Discussion

If the texture isn’t a 3D texture, then Metal ignores this property.

The default value is `0`.

## See Also

### Specifying the texture for the attachment
- [var texture: (any MTLTexture)?](./texture.md)
  The texture object associated with this attachment.
- [var level: Int](./level.md)
  The mipmap level of the texture used for rendering to the attachment.
- [var slice: Int](./slice.md)
  The slice of the texture used for rendering to the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/depthplane)*