# encode(_:using:)

**Framework**: Tabulardata  
**Kind**: method

Encodes each element of the column.

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
mutating func encode<T, Encoder>(_ type: T.Type, using encoder: Encoder) throws where T : Encodable, Encoder : TopLevelEncoder
```

#### Discussion

> **Note**: `ColumnEncodingError` if an element fails to encode.

## Parameters

- `type`: The type of elements in the column.
- `encoder`: An encoder.

## See Also

- [func encoded<T, Encoder>(T.Type, using: Encoder) throws -> AnyColumn](anycolumn/encoded(_:using:).md)
  Generates a column by encoding each element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/encode(_:using:))*