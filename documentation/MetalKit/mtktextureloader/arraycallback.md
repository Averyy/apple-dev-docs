# MTKTextureLoader.ArrayCallback

**Framework**: MetalKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block executed after an asynchronous loading operation for multiple textures has completed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias ArrayCallback = ([any MTLTexture], (any Error)?) -> Void
```

```c
typedef void (^)(NSArray<id<MTLTexture>> *, NSError *) MTKTextureLoaderArrayCallback;
```

#### Discussion

The block parameters are defined as follows:

- **textures**: An array of [`MTLTexture`](../../Metal/mtltexture.md) objects whose order corresponds to the requested textures. If an error occurs when loading a texture, an [`NSNull`](../../Foundation/nsnull.md) object occupies its place in the array.
- **error**: If all texture loading operations were successful, this value is `nil`; otherwise, this parameter holds an [`NSError`](../../Foundation/nserror.md) object that describes the first problem that occurred. (Which element in the input array the error corresponds to is undefined.)

## See Also

### Completing a Texture Loading Operation
- [MTKTextureLoader.Callback](./callback.md)
  The signature for the block executed after an asynchronous loading operation for a single texture has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/arraycallback)*