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

## See Also

- [MTKTextureLoader.Callback](mtktextureloader/callback.md)
  The signature for the block executed after an asynchronous loading operation for a single texture has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/arraycallback)*