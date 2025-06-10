# MTLSamplerAddressMode

**Framework**: Metal  
**Kind**: enum

Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLSamplerAddressMode
```

## Topics

### Address Mode Options
- [MTLSamplerAddressMode.clampToEdge](mtlsampleraddressmode/clamptoedge.md)
  Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressMode.mirrorClampToEdge](mtlsampleraddressmode/mirrorclamptoedge.md)
  Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.
- [MTLSamplerAddressMode.repeat](mtlsampleraddressmode/repeat.md)
  Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressMode.mirrorRepeat](mtlsampleraddressmode/mirrorrepeat.md)
  Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressMode.clampToZero](mtlsampleraddressmode/clamptozero.md)
  Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
- [MTLSamplerAddressMode.clampToBorderColor](mtlsampleraddressmode/clamptobordercolor.md)
  Out-of-range texture coordinates return the value specified by the [`borderColor`](mtlsamplerdescriptor/bordercolor.md) property.
### Initializers
- [init?(rawValue: UInt)](mtlsampleraddressmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var rAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/raddressmode.md)
  The address mode for the texture depth (r) coordinate.
- [var sAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/saddressmode.md)
  The address mode for the texture width (s) coordinate.
- [var tAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/taddressmode.md)
  The address mode for the texture height (t) coordinate.
- [var borderColor: MTLSamplerBorderColor](mtlsamplerdescriptor/bordercolor.md)
  The border color for clamped texture values.
- [enum MTLSamplerBorderColor](mtlsamplerbordercolor.md)
  Values that determine the border color for clamped texture values when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsampleraddressmode)*