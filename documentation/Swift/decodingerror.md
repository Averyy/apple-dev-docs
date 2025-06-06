# DecodingError

**Framework**: Swift  
**Kind**: enum

An error that occurs during the decoding of a value.

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
enum DecodingError
```

## Topics

### Structures
- [DecodingError.Context](decodingerror/context.md)
  The context in which the error occurred.
### Enumeration Cases
- [case dataCorrupted(DecodingError.Context)](decodingerror/datacorrupted(_:).md)
  An indication that the data is corrupted or otherwise invalid.
- [case keyNotFound(any CodingKey, DecodingError.Context)](decodingerror/keynotfound(_:_:).md)
  An indication that a keyed decoding container was asked for an entry for the given key, but did not contain one.
- [case typeMismatch(any Any.Type, DecodingError.Context)](decodingerror/typemismatch(_:_:).md)
  An indication that a value of the given type could not be decoded because it did not match the type of what was found in the encoded payload.
- [case valueNotFound(any Any.Type, DecodingError.Context)](decodingerror/valuenotfound(_:_:).md)
  An indication that a non-optional value of the given type was expected, but a null value was found.
### Type Methods
- [static func dataCorruptedError<C>(forKey: C.Key, in: C, debugDescription: String) -> DecodingError](decodingerror/datacorruptederror(forkey:in:debugdescription:).md)
  Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.
- [static func dataCorruptedError(in: any SingleValueDecodingContainer, debugDescription: String) -> DecodingError](decodingerror/datacorruptederror(in:debugdescription:)-4ruvu.md)
  Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.
- [static func dataCorruptedError(in: any UnkeyedDecodingContainer, debugDescription: String) -> DecodingError](decodingerror/datacorruptederror(in:debugdescription:)-5on9z.md)
  Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

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
- [enum EncodingError](encodingerror.md)
  An error that occurs during the encoding of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decodingerror)*