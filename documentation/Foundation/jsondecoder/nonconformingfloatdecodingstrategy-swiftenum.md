# JSONDecoder.NonConformingFloatDecodingStrategy

**Framework**: Foundation  
**Kind**: enum

The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum NonConformingFloatDecodingStrategy
```

#### Overview

The IEEE 754 floating-point specification defines exceptional values, which include [`infinity`](https://developer.apple.com/documentation/Swift/FloatingPoint/infinity) and [`nan`](https://developer.apple.com/documentation/Swift/FloatingPoint/nan).

## Topics

### Exceptional Values
- [JSONDecoder.NonConformingFloatDecodingStrategy.convertFromString(positiveInfinity:negativeInfinity:nan:)](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum/convertfromstring(positiveinfinity:negativeinfinity:nan:).md)
  The strategy that decodes exceptional floating-point values from a specified string representation.
- [JSONDecoder.NonConformingFloatDecodingStrategy.throw](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum/throw.md)
  The strategy that throws an error upon decoding an exceptional floating-point value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var nonConformingFloatDecodingStrategy: JSONDecoder.NonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.property.md)
  The strategy used by a decoder when it encounters exceptional floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.enum)*