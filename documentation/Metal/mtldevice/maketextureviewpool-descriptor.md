# makeTextureViewPool(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new texture view pool from a resource view pool descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeTextureViewPool(descriptor: MTLResourceViewPoolDescriptor) throws -> any MTLTextureViewPool
```

#### Return Value

A [`MTLTextureViewPool`](mtltextureviewpool.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures the    instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketextureviewpool(descriptor:))*