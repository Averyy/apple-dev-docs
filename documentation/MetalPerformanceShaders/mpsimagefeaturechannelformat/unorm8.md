# MPSImageFeatureChannelFormat.unorm8

**Framework**: Metal Performance Shaders  
**Kind**: case  
**Role**: Case

`uint8_t` type with value `[0,255]` and encoding `[0,1.0]`.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case unorm8
```

```c
MPSImageFeatureChannelFormatUnorm8
```

## See Also

### Constants
- [MPSImageFeatureChannelFormat.none](./none.md)
- [MPSImageFeatureChannelFormat.unorm16](./unorm16.md)
  `uint16_t` type with value `[0,65535]` and encoding `[0,1.0]`.
- [MPSImageFeatureChannelFormat.float16](./float16.md)
  IEEE-754 16-bit floating-point type (half precision). Representable normal range is `+-[2^-14, 65504], 0, INF, NaN`. 11 bits of precision + exponent.
- [MPSImageFeatureChannelFormat.float32](./float32.md)
  IEEE-754 32-bit floating-point type (single precision, standard `float` type in C). 24 bits of precision + exponent.
- [MPSImageFeatureChannelFormat_reserved0](./mpsimagefeaturechannelformat_reserved0.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/unorm8)*