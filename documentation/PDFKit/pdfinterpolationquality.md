# PDFInterpolationQuality

**Framework**: PDFKit  
**Kind**: enum

A wrapper for the specified interpolation quality.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFInterpolationQuality
```

## Topics

### Enumeration Cases
- [PDFInterpolationQuality.none](pdfinterpolationquality/none.md)
  The case where no interpolation quality is specified.
- [PDFInterpolationQuality.low](pdfinterpolationquality/low.md)
  The case specifying low interpolation quality.
- [PDFInterpolationQuality.high](pdfinterpolationquality/high.md)
  The case specifying high interpolation quality.
### Initializers
- [init?(rawValue: Int)](pdfinterpolationquality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var shouldAntiAlias: Bool](pdfview/shouldantialias.md)
  A Boolean value indicating whether the view is antialiased.
- [var interpolationQuality: PDFInterpolationQuality](pdfview/interpolationquality.md)
  The interpolation quality for images drawn into the `PDFView` context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfinterpolationquality)*