# copyAsync(to:completionHandler:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously copies texture data to another texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func copyAsync(to texture: any MTLTexture, completionHandler: @escaping @MainActor ((any Error)?) -> Void)
```

#### Discussion

This function is asynchronous. It returns immediately and runs in the background, calling `completionHandler` when it finishes or errors. This method copies all available mipmap sizes to `texture`.

It’s recommended that you provide a value for [`semantic`](textureresource/createoptions/semantic.md) when creating this resource. Specifying a semantic enables RealityKit to select an appropriate pixel format for the target texture.

## Parameters

- `texture`: The target texture for copying the data.   It needs to have the same width and height as  , and    usage.
- `completionHandler`: The system calls this closure after it finishes copying the data, with a   error if it succeeds.

## See Also

- [func copy(to: any MTLTexture) async throws](textureresource/copy(to:)-3lfen.md)
  Asynchronously copies texture data to another texture.
- [func copy(to: any MTLTexture) throws](textureresource/copy(to:)-jfbi.md)
  Copies texture data to another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/copyasync(to:completionhandler:))*