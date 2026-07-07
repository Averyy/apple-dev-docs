# swizzle

**Framework**: RealityKit  
**Kind**: property

The channel swizzle pattern the GPU applies when sampling the texture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var swizzle: MTLTextureSwizzleChannels { get set }
```

#### Discussion

Corresponds to `MTLTextureDescriptor.swizzle`.

## See Also

- [var textureUsage: MTLTextureUsage](lowleveltextureresource/descriptor-swift.struct/textureusage.md)
  The options that determine how the texture can be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct/swizzle)*