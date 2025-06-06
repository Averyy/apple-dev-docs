# MTLSamplerMipFilter.notMipmapped

**Framework**: Metal  
**Kind**: case

The texture is sampled from mipmap level `0`, and other mipmap levels are ignored.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case notMipmapped
```

## See Also

- [MTLSamplerMipFilter.nearest](mtlsamplermipfilter/nearest.md)
  The nearest mipmap level is selected.
- [MTLSamplerMipFilter.linear](mtlsamplermipfilter/linear.md)
  If the filter falls between mipmap levels, both levels are sampled and the results are determined by linear interpolation between levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplermipfilter/notmipmapped)*