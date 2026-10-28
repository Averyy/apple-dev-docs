# number

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A style for formatting 32-bit unsigned integers.

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
static var number: IntegerFormatStyle<UInt32> { get }
```

Available when `Self` is `IntegerFormatStyle<UInt32>`.

## Discussion

Use this type property when the call point allows the use of [`IntegerFormatStyle`](../integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [`BinaryInteger`](../../Swift/binaryinteger.md).

## See Also

### Applying numeric styles for integers
- [static var number: IntegerFormatStyle<Int>](./number-7fxvo.md)
  A style for formatting the Swift default integer type.
- [static var number: IntegerFormatStyle<UInt>](./number-4ttgp.md)
  A style for formatting the Swift unsigned integer type.
- [static var number: IntegerFormatStyle<Int8>](./number-5hzgj.md)
  A style for formatting 8-bit signed integers.
- [static var number: IntegerFormatStyle<Int16>](./number-1o8fx.md)
  A style for formatting 16-bit signed integers.
- [static var number: IntegerFormatStyle<Int32>](./number-4cj49.md)
  A style for formatting 32-bit signed integers.
- [static var number: IntegerFormatStyle<Int64>](./number-3925i.md)
  A style for formatting 64-bit signed integers.
- [static var number: IntegerFormatStyle<UInt8>](./number-8fms6.md)
  A style for formatting 8-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt16>](./number-fak0.md)
  A style for formatting 16-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt64>](./number-iyry.md)
  A style for formatting 64-bit unsigned integers.
- [struct IntegerFormatStyle](../integerformatstyle.md)
  A structure that converts between integer values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/number-13mra)*