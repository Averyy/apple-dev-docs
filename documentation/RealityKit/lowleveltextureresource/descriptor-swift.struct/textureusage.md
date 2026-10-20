# textureUsage

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The options that determine how the texture can be used.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var textureUsage: MTLTextureUsage { get set }
```

#### Discussion

Corresponds to `MTLTextureDescriptor.usage`.

## See Also

### Configuring texture usage
- [var swizzle: MTLTextureSwizzleChannels](./swizzle.md)
  The channel swizzle pattern the GPU applies when sampling the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct/textureusage)*