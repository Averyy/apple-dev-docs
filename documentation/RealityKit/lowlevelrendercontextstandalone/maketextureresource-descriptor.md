# makeTextureResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Creates a texture resource from the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource
```

#### Return Value

A newly created [`LowLevelTextureResource`](lowleveltextureresource.md).

#### Discussion

> **Note**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The texture type, pixel format, dimensions, and usage flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/maketextureresource(descriptor:))*