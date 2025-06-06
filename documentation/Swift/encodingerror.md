# EncodingError

**Framework**: Swift  
**Kind**: enum

An error that occurs during the encoding of a value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum EncodingError
```

## Topics

### Structures
- [EncodingError.Context](encodingerror/context.md)
  The context in which the error occurred.
### Enumeration Cases
- [case invalidValue(Any, EncodingError.Context)](encodingerror/invalidvalue(_:_:).md)
  An indication that an encoder or its containers could not encode the given value.

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Error](error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](sendable.md)

## See Also

- [protocol Encoder](encoder.md)
  A type that can encode values into a native format for external representation.
- [protocol Decoder](decoder.md)
  A type that can decode values from a native format into in-memory representations.
- [enum DecodingError](decodingerror.md)
  An error that occurs during the decoding of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encodingerror)*