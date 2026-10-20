# copy(to:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously copies texture data to another texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func copy(to texture: any MTLTexture) async throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func copy(to texture: any MTLTexture) throws
```

#### Discussion

This method copies all available mipmap sizes to `texture`.

It’s recommended that you provide a value for [`semantic`](./createoptions/semantic.md) when creating this resource. Specifying a semantic enables RealityKit to select an appropriate pixel format for the target texture.

## Parameters

- `texture`: The target texture for copying the data. It needs to have the same width and height as [`TextureResource`](../textureresource.md), and [`shaderWrite`](../../Metal/mtltextureusage/shaderwrite.md) usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/copy(to:))*