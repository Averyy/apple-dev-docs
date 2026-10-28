# slice

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The slice of the texture used for rendering to the attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var slice: Int { get set }
```

```objc
@property (nonatomic) NSUInteger slice;
```

## Discussion

The default value is `0`.

## See Also

### Specifying the texture for the attachment
- [var texture: (any MTLTexture)?](./texture.md)
  The texture object associated with this attachment.
- [var level: Int](./level.md)
  The mipmap level of the texture used for rendering to the attachment.
- [var depthPlane: Int](./depthplane.md)
  The depth plane of the texture used for rendering to the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/slice)*