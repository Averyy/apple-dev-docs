# MTLSamplerMinMagFilter.linear

**Framework**: Metal  
**Kind**: case

Select two pixels in each dimension and interpolate linearly between them.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case linear
```

#### Discussion

Support for linear filtering varies by GPU and the format of the texture being sampled. For example, you can’t use linear filtering on textures with an integer format, and only some device objects support linear filtering for textures with a floating-point format. To determine whether linear filtering is available for a specific texture format, see:

- [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [`Metal feature set tables (Numbers)`](https://developer.apple.comhttps://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

- [MTLSamplerMinMagFilter.nearest](mtlsamplerminmagfilter/nearest.md)
  Select the single pixel nearest to the sample point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter/linear)*