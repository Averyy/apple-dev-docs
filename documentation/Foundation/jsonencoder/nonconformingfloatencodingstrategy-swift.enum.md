# JSONEncoder.NonConformingFloatEncodingStrategy

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
enum NonConformingFloatEncodingStrategy
```

## Overview

The IEEE 754 floating-point specification defines exceptional values, which include [`infinity`](../../Swift/floatingpoint/infinity.md) and [`nan`](../../Swift/floatingpoint/nan.md).

## Topics

### Exceptional Values
- [JSONEncoder.NonConformingFloatEncodingStrategy.convertToString(positiveInfinity:negativeInfinity:nan:)](./nonconformingfloatencodingstrategy-swift.enum/converttostring%28positiveinfinity,negativeinfinity,nan%29.md)
  The strategy that encodes exceptional floating-point values from a specified string representation.
- [JSONEncoder.NonConformingFloatEncodingStrategy.throw](./nonconformingfloatencodingstrategy-swift.enum/throw.md)
  The strategy that throws an error upon encoding an exceptional floating-point value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Encoding Exceptional Numbers
- [var nonConformingFloatEncodingStrategy: JSONEncoder.NonConformingFloatEncodingStrategy](./nonconformingfloatencodingstrategy-swift.property.md)
  The strategy used by an encoder when it encounters exceptional floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.enum)*