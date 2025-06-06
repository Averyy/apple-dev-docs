# MTLAttributeFormat.floatRG11B10

**Framework**: Metal  
**Kind**: case

One packed 32-bit value representing pixel data containing 11-bit float red and green channels, and a 10-bit float blue channel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case floatRG11B10
```

#### Discussion

This data format is identical to [`MTLPixelFormat.rg11b10Float`](mtlpixelformat/rg11b10float.md), and used in compute functions for manipulating pixels.

## See Also

- [MTLAttributeFormat.uchar4Normalized_bgra](mtlattributeformat/uchar4normalized_bgra.md)
  Four unsigned normalized 8-bit values, arranged as blue, green, red, and alpha components.
- [MTLAttributeFormat.floatRGB9E5](mtlattributeformat/floatrgb9e5.md)
  One packed 32-bit value representing pixel data containing 9-bit float red, green, and blue channels, and a 5-bit float shared exponent channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributeformat/floatrg11b10)*