# makeTextureViewPool(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new texture view pool from a resource view pool descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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