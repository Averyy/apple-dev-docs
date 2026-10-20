# MTLSamplerAddressMode.clampToZero

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case clampToZero
```

```c
MTLSamplerAddressModeClampToZero
```

## See Also

### Address mode options
- [MTLSamplerAddressMode.clampToEdge](./clamptoedge.md)
  Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressMode.mirrorClampToEdge](./mirrorclamptoedge.md)
  Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressMode.repeat](./repeat.md)
  Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressMode.mirrorRepeat](./mirrorrepeat.md)
  Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressMode.clampToBorderColor](./clamptobordercolor.md)
  An address mode that returns the sampler’s border color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/clamptozero)*