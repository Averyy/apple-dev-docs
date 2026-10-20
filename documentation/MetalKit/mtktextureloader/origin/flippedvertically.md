# flippedVertically

**Framework**: MetalKit  
**Kind**: property  
**Role**: Type Property

An option that specifies that images should always be flipped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let flippedVertically: MTKTextureLoader.Origin
```

```c
extern MTKTextureLoaderOrigin const MTKTextureLoaderOriginFlippedVertically;
```

#### Discussion

The texture will be flipped vertically regardless of any metadata in the file indicating the placement of the origin in the source data.

## See Also

### Specifying Texture Origin Options
- [static let topLeft: MTKTextureLoader.Origin](./topleft.md)
  An option for specifying images that should be flipped only to put their origin in the top-left corner.
- [static let bottomLeft: MTKTextureLoader.Origin](./bottomleft.md)
  An option for specifying images that should be flipped only to put their origin in the bottom-left corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/origin/flippedvertically)*