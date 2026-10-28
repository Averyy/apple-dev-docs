# MTKTextureLoader.Callback

**Framework**: MetalKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block executed after an asynchronous loading operation for a single texture has completed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias Callback = ((any MTLTexture)?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLTexture>, NSError *) MTKTextureLoaderCallback;
```

## Discussion

The block parameters are defined as follows:

- **texture**: A [`MTLTexture`](../../Metal/mtltexture.md) object, or `nil` if an error occurred.
- **error**: If the operation was successful, this value is `nil`; otherwise, this parameter holds an [`NSError`](../../Foundation/nserror.md) object that describes the problem that occurred.

## See Also

### Completing a Texture Loading Operation
- [MTKTextureLoader.ArrayCallback](./arraycallback.md)
  The signature for the block executed after an asynchronous loading operation for multiple textures has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/callback)*