# JSONDecoder.NonConformingFloatDecodingStrategy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

The IEEE 754 floating-point specification defines exceptional values, which include [`infinity`](../../Swift/floatingpoint/infinity.md) and [`nan`](../../Swift/floatingpoint/nan.md).

## Topics

### Exceptional Values
- [JSONDecoder.NonConformingFloatDecodingStrategy.convertFromString(positiveInfinity:negativeInfinity:nan:)](./nonconformingfloatdecodingstrategy-swift.enum/convertfromstring%28positiveinfinity,negativeinfinity,nan%29.md)
  The strategy that decodes exceptional floating-point values from a specified string representation.
- [JSONDecoder.NonConformingFloatDecodingStrategy.throw](./nonconformingfloatdecodingstrategy-swift.enum/throw.md)
  The strategy that throws an error upon decoding an exceptional floating-point value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Decoding Exceptional Numbers
- [var nonConformingFloatDecodingStrategy: JSONDecoder.NonConformingFloatDecodingStrategy](./nonconformingfloatdecodingstrategy-swift.property.md)
  The strategy used by a decoder when it encounters exceptional floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.enum)*