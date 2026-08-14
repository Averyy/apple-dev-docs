# MTLTextureViewDescriptor

**Framework**: Metal  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTLTextureViewDescriptor
```

## Topics

### Instance Properties
- [var levelRange: Range<Int>](mtltextureviewdescriptor/levelrange-55q8m.md)
  A desired range of mip levels of a texture view.
- [var pixelFormat: MTLPixelFormat](mtltextureviewdescriptor/pixelformat.md)
- [var sliceRange: Range<Int>](mtltextureviewdescriptor/slicerange-6nq6v.md)
  A desired range of slices of a texture view.
- [var swizzle: MTLTextureSwizzleChannels](mtltextureviewdescriptor/swizzle.md)
- [var textureType: MTLTextureType](mtltextureviewdescriptor/texturetype.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [class MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md)
  Provides parameters for creating a resource view pool.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewdescriptor)*