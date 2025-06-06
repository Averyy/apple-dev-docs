# kCVImageBufferChromaSubsampling_420

**Framework**: Core Video  
**Kind**: var

A key that indicates the original chroma-subsampled data used 4:2:0 formatting.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCVImageBufferChromaSubsampling_420: CFString
```

#### Discussion

Each pixel has a `Y` value, and `U` and `V` values are shared within a square of 4 pixels.

## See Also

- [let kCVImageBufferChromaSubsampling_422: CFString](kcvimagebufferchromasubsampling_422.md)
  A key that indicates the original chroma-subsampled data used 4:2:2 formatting.
- [let kCVImageBufferChromaSubsampling_411: CFString](kcvimagebufferchromasubsampling_411.md)
  A key that indicates the original chroma-subsampled data used 4:1:1 formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsampling_420)*