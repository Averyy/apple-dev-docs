# MTLTextureViewPool

**Framework**: Metal  
**Kind**: protocol

A pool of lightweight texture views.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTLTextureViewPool : MTLResourceViewPool
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Use texture view pools to create lightweight texture view objects of [`MTLTexture`](mtltexture.md) and [`MTLBuffer`](mtlbuffer.md) instances.

## Topics

### Instance Methods
- [func setTextureView(buffer: any MTLBuffer, descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int, index: Int) -> MTLResourceID](mtltextureviewpool/settextureview(buffer:descriptor:offset:bytesperrow:index:).md)
  Creates a new lightweight texture view of a buffer.
- [func setTextureView(texture: any MTLTexture, descriptor: MTLTextureViewDescriptor, index: Int) -> MTLResourceID](mtltextureviewpool/settextureview(texture:descriptor:index:).md)
  Creates a new lightweight texture view.
- [func setTextureView(texture: any MTLTexture, index: Int) -> MTLResourceID](mtltextureviewpool/settextureview(texture:index:).md)
  Copies a default texture view to a slot in this texture view pool at an index provided.

## Relationships

### Inherits From
- [MTLResourceViewPool](mtlresourceviewpool.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [class MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md)
  Provides parameters for creating a resource view pool.
- [class MTLTextureViewDescriptor](mtltextureviewdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewpool)*