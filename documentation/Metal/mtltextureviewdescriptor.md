# MTLTextureViewDescriptor

**Framework**: Metal  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [class MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md)
  Provides parameters for creating a resource view pool.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewdescriptor)*