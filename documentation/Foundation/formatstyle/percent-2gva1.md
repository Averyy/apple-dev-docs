# percent

**Framework**: Foundation  
**Kind**: property

A style for formatting the Swift standard single-precision floating-point type as a percent representation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var percent: FloatingPointFormatStyle<Float>.Percent { get }
```

#### Discussion

Use this type property when the call point allows the use of [`FloatingPointFormatStyle`](floatingpointformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint).

## See Also

- [static var percent: FloatingPointFormatStyle<Double>.Percent](formatstyle/percent-6cwuv.md)
  A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [static var percent: FloatingPointFormatStyle<Float16>.Percent](formatstyle/percent-grss.md)
  A style for formatting 16-bit floating-point values as a percent representation.
- [FloatingPointFormatStyle.Percent](floatingpointformatstyle/percent.md)
  A format style that converts between floating-point percentage values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/percent-2gva1)*