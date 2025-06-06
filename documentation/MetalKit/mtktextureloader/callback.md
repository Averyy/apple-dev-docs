# MTKTextureLoader.Callback

**Framework**: MetalKit  
**Kind**: typealias

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

#### Discussion

The block parameters are defined as follows:

## See Also

- [MTKTextureLoader.ArrayCallback](mtktextureloader/arraycallback.md)
  The signature for the block executed after an asynchronous loading operation for multiple textures has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/callback)*