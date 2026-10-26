# MPSImageFeatureChannelFormat_reserved0

**Framework**: Metal Performance Shaders  
**Kind**: case  
**Role**: Enumeration Case

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```c
MPSImageFeatureChannelFormat_reserved0
```

## See Also

### Constants
- [MPSImageFeatureChannelFormat.none](./none.md)
- [MPSImageFeatureChannelFormat.unorm8](./unorm8.md)
  `uint8_t` type with value `[0,255]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.unorm16](./unorm16.md)
  `uint16_t` type with value `[0,65535]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.float16](./float16.md)
  IEEE-754 16-bit floating-point type (half precision). Representable normal range is `+-[2^-14, 65504], 0, INF, NaN`. 11 bits of precision + exponent.
- [MPSImageFeatureChannelFormat.float32](./float32.md)
  IEEE-754 32-bit floating-point type (single precision, standard `float` type in C). 24 bits of precision + exponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/mpsimagefeaturechannelformat_reserved0)*