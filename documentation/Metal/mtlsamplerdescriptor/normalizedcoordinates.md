# normalizedCoordinates

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether texture coordinates are normalized to the range `[0.0, 1.0]`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var normalizedCoordinates: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), texture coordinates are from `0.0` to `1.0`. If [`false`](https://developer.apple.com/documentation/Swift/false), texture coordinates are from `0` to `width` for horizontal coordinates and `0` to `height` for vertical coordinates. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

Non-normalized texture coordinates should only be used with 1D and 2D textures with the following conditions; otherwise, the results of sampling are undefined.

- The [`MTLSamplerAddressMode.clampToEdge`](mtlsampleraddressmode/clamptoedge.md) or [`MTLSamplerAddressMode.clampToZero`](mtlsampleraddressmode/clamptozero.md) address mode.
- The [`MTLSamplerMipFilter.notMipmapped`](mtlsamplermipfilter/notmipmapped.md) mipmap filtering option.
- [`minFilter`](mtlsamplerdescriptor/minfilter.md) and [`magFilter`](mtlsamplerdescriptor/magfilter.md) need to be equal to each other.
- [`maxAnisotropy`](mtlsamplerdescriptor/maxanisotropy.md) needs to be `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/normalizedcoordinates)*