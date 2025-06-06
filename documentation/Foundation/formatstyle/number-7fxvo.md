# number

**Framework**: Foundation  
**Kind**: property

A style for formatting the Swift default integer type.

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
static var number: IntegerFormatStyle<Int> { get }
```

#### Discussion

Use this type property when the call point allows the use of [`IntegerFormatStyle`](integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger).

## See Also

- [static var number: IntegerFormatStyle<UInt>](formatstyle/number-4ttgp.md)
  A style for formatting the Swift unsigned integer type.
- [static var number: IntegerFormatStyle<Int8>](formatstyle/number-5hzgj.md)
  A style for formatting 8-bit signed integers.
- [static var number: IntegerFormatStyle<Int16>](formatstyle/number-1o8fx.md)
  A style for formatting 16-bit signed integers.
- [static var number: IntegerFormatStyle<Int32>](formatstyle/number-4cj49.md)
  A style for formatting 32-bit signed integers.
- [static var number: IntegerFormatStyle<Int64>](formatstyle/number-3925i.md)
  A style for formatting 64-bit signed integers.
- [static var number: IntegerFormatStyle<UInt8>](formatstyle/number-8fms6.md)
  A style for formatting 8-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt16>](formatstyle/number-fak0.md)
  A style for formatting 16-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt32>](formatstyle/number-13mra.md)
  A style for formatting 32-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt64>](formatstyle/number-iyry.md)
  A style for formatting 64-bit unsigned integers.
- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/number-7fxvo)*