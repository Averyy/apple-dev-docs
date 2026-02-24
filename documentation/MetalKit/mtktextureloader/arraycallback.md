# MTKTextureLoader.ArrayCallback

**Framework**: MetalKit  
**Kind**: typealias

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

#### Discussion

The block parameters are defined as follows:

- **textures**: An array of [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) objects whose order corresponds to the requested textures. If an error occurs when loading a texture, an [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object occupies its place in the array.
- **error**: If all texture loading operations were successful, this value is `nil`; otherwise, this parameter holds an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that describes the first problem that occurred. (Which element in the input array the error corresponds to is undefined.)

## See Also

- [MTKTextureLoader.Callback](mtktextureloader/callback.md)
  The signature for the block executed after an asynchronous loading operation for a single texture has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/arraycallback)*