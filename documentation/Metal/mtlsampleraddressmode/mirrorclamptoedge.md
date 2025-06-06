# MTLSamplerAddressMode.mirrorClampToEdge

**Framework**: Metal  
**Kind**: case

Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, texture coordinates are clamped.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.11+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case mirrorClampToEdge
```

## See Also

- [MTLSamplerAddressMode.clampToEdge](mtlsampleraddressmode/clamptoedge.md)
  Texture coordinates are clamped between `0.0` and `1.0`, inclusive.
- [MTLSamplerAddressMode.repeat](mtlsampleraddressmode/repeat.md)
  Texture coordinates wrap to the other side of the texture, effectively keeping only the fractional part of the texture coordinate.
- [MTLSamplerAddressMode.mirrorRepeat](mtlsampleraddressmode/mirrorrepeat.md)
  Between `-1.0` and `1.0`, the texture coordinates are mirrored across the axis; outside `-1.0` and `1.0`, the image is repeated.
- [MTLSamplerAddressMode.clampToZero](mtlsampleraddressmode/clamptozero.md)
  Out-of-range texture coordinates return transparent zero `(0,0,0,0)` for images with an alpha channel and return opaque zero `(0,0,0,1)` for images without an alpha channel.
- [MTLSamplerAddressMode.clampToBorderColor](mtlsampleraddressmode/clamptobordercolor.md)
  Out-of-range texture coordinates return the value specified by the [`borderColor`](mtlsamplerdescriptor/bordercolor.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/mirrorclamptoedge)*