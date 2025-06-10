# init(descriptor:)

**Framework**: RealityKit  
**Kind**: init

Creates a low-level texture from a descriptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(descriptor: LowLevelTexture.Descriptor) throws
```

#### Discussion

> **Note**: If the descriptor is invalid or if memory was not allocated successfully.

## Parameters

- `descriptor`: An object that defines the structure of the low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltexture/init(descriptor:))*