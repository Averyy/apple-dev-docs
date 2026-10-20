# swizzle

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The channel swizzle pattern the GPU applies when sampling the texture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var swizzle: MTLTextureSwizzleChannels { get set }
```

#### Discussion

Corresponds to `MTLTextureDescriptor.swizzle`.

## See Also

### Configuring texture usage
- [var textureUsage: MTLTextureUsage](./textureusage.md)
  The options that determine how the texture can be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource/descriptor-swift.struct/swizzle)*