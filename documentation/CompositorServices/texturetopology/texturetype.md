# textureType

**Framework**: Compositor Services  
**Kind**: property

The texture type value that specifies how the underlying texture organizes its views.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var textureType: MTLTextureType { get }
```

#### Discussion

A texture might store the content of one view or multiple views. For example, a single texture might store one or both views for the left and right eyes of a head-mounted display. The texture type indicates this content organization strategy.

## See Also

- [var arrayLength: UInt64](texturetopology/arraylength.md)
  The number of items in the texture array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/texturetopology/texturetype)*