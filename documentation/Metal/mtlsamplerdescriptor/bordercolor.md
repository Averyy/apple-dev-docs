# borderColor

**Framework**: Metal  
**Kind**: property

The border color for clamped texture values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.12+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var borderColor: MTLSamplerBorderColor { get set }
```

#### Discussion

This value is only used when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).

## See Also

- [var rAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/raddressmode.md)
  The address mode for the texture depth (r) coordinate.
- [var sAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/saddressmode.md)
  The address mode for the texture width (s) coordinate.
- [var tAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/taddressmode.md)
  The address mode for the texture height (t) coordinate.
- [enum MTLSamplerAddressMode](mtlsampleraddressmode.md)
  Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [enum MTLSamplerBorderColor](mtlsamplerbordercolor.md)
  Values that determine the border color for clamped texture values when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/bordercolor)*