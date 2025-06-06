# kCVImageBufferChromaSubsampling_411

**Framework**: Core Video  
**Kind**: var

A key that indicates the original chroma-subsampled data used 4:1:1 formatting.

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
let kCVImageBufferChromaSubsampling_411: CFString
```

#### Discussion

Each pixel has a `Y` value, and `U` and `V` values are shared along a horizontal line of 4 pixels.

## See Also

- [let kCVImageBufferChromaSubsampling_420: CFString](kcvimagebufferchromasubsampling_420.md)
  A key that indicates the original chroma-subsampled data used 4:2:0 formatting.
- [let kCVImageBufferChromaSubsampling_422: CFString](kcvimagebufferchromasubsampling_422.md)
  A key that indicates the original chroma-subsampled data used 4:2:2 formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsampling_411)*