# rAddressMode

**Framework**: Metal  
**Kind**: property

The address mode for the texture depth (r) coordinate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var rAddressMode: MTLSamplerAddressMode { get set }
```

#### Discussion

The default value is [`MTLSamplerAddressMode.clampToEdge`](mtlsampleraddressmode/clamptoedge.md).

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var sAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/saddressmode.md)
  The address mode for the texture width (s) coordinate.
- [var tAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/taddressmode.md)
  The address mode for the texture height (t) coordinate.
- [var borderColor: MTLSamplerBorderColor](mtlsamplerdescriptor/bordercolor.md)
  The border color for clamped texture values.
- [enum MTLSamplerAddressMode](mtlsampleraddressmode.md)
  Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [enum MTLSamplerBorderColor](mtlsamplerbordercolor.md)
  Values that determine the border color for clamped texture values when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/raddressmode)*