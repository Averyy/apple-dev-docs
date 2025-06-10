# arrayLength

**Framework**: Compositor Services  
**Kind**: property

The number of items in the texture array.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var arrayLength: UInt64 { get }
```

#### Discussion

Array-based texture types such as [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray) manage one or more images of the same size. The array length represents the number of separate images the texture manages. Other array types store only one image.

## See Also

- [var textureType: MTLTextureType](texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/texturetopology/arraylength)*