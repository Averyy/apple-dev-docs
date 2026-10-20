# number

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A style for formatting the Swift standard double-precision floating-point type.

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
static var number: FloatingPointFormatStyle<Double> { get }
```

Available when `Self` is `FloatingPointFormatStyle<Double>`.

#### Discussion

Use this type property when the call point allows the use of [`FloatingPointFormatStyle`](../floatingpointformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [`BinaryFloatingPoint`](../../Swift/binaryfloatingpoint.md).

## See Also

### Applying numeric styles for floating-point values
- [static var number: FloatingPointFormatStyle<Float>](./number-432x3.md)
  A style for formatting the Swift standard single-precision floating-point type.
- [static var number: FloatingPointFormatStyle<Float16>](./number-3qe2o.md)
  A style for formatting 16-bit floating-point values.
- [struct FloatingPointFormatStyle](../floatingpointformatstyle.md)
  A structure that converts between floating-point values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/number-8c8rj)*