# swizzle

**Framework**: RealityKit  
**Kind**: property

Channel swizzle to use when RealityKit reads or samples from the texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var swizzle: MTLTextureSwizzleChannels
```

#### Discussion

The default value performs no swizzle, sampling red from the texture’s red channel, green from the texture’s green channel, blue from the texture’s blue channel, and alpha from the texture’s alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparameters/texture/swizzle)*