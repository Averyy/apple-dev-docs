# MTLSamplerAddressMode.clampToBorderColor

**Framework**: Metal  
**Kind**: case

Out-of-range texture coordinates return the value specified by the [`borderColor`](mtlsamplerdescriptor/bordercolor.md) property.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.12+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case clampToBorderColor
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/clamptobordercolor)*