# MTLSamplerBorderColor

**Framework**: Metal  
**Kind**: enum

Values that determine the border color for clamped texture values when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.12+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLSamplerBorderColor
```

## Topics

### Specifying Border Color Options
- [MTLSamplerBorderColor.transparentBlack](mtlsamplerbordercolor/transparentblack.md)
  A transparent black color `(0,0,0,0)` for texture values outside the border.
- [MTLSamplerBorderColor.opaqueBlack](mtlsamplerbordercolor/opaqueblack.md)
  An opaque black color `(0,0,0,1)` for texture values outside the border
- [MTLSamplerBorderColor.opaqueWhite](mtlsamplerbordercolor/opaquewhite.md)
  An opaque white color `(1,1,1,1)` for texture values outside the border.
### Initializers
- [init?(rawValue: UInt)](mtlsamplerbordercolor/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var rAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/raddressmode.md)
  The address mode for the texture depth (r) coordinate.
- [var sAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/saddressmode.md)
  The address mode for the texture width (s) coordinate.
- [var tAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/taddressmode.md)
  The address mode for the texture height (t) coordinate.
- [var borderColor: MTLSamplerBorderColor](mtlsamplerdescriptor/bordercolor.md)
  The border color for clamped texture values.
- [enum MTLSamplerAddressMode](mtlsampleraddressmode.md)
  Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor)*