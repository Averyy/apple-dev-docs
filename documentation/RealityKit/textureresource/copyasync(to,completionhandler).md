# copyAsync(to:completionHandler:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously copies texture data to another texture.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: copy(to:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: copy(to:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: copy(to:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: copy(to:))
- tvOS 26.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: copy(to:))

## Declaration

```swift
@MainActor
@preconcurrency func copyAsync(to texture: any MTLTexture, completionHandler: @escaping @MainActor ((any Error)?) -> Void)
```

#### Discussion

This function is asynchronous. It returns immediately and runs in the background, calling `completionHandler` when it finishes or errors. This method copies all available mipmap sizes to `texture`.

It’s recommended that you provide a value for [`semantic`](./createoptions/semantic.md) when creating this resource. Specifying a semantic enables RealityKit to select an appropriate pixel format for the target texture.

## Parameters

- `texture`: The target texture for copying the data. It needs to have the same width and height as [`TextureResource`](../textureresource.md), and [`shaderWrite`](../../Metal/mtltextureusage/shaderwrite.md) usage.
- `completionHandler`: The system calls this closure after it finishes copying the data, with a `nil` error if it succeeds.

## See Also

### Copying the texture
- [func copy(to: any MTLTexture) throws](./copy%28to%29-jfbi.md)
  Copies texture data to another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/copyasync(to:completionhandler:))*