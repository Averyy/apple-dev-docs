# decode(_:using:)

**Framework**: Tabulardata  
**Kind**: method

Decodes the data in each element of the column.

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
mutating func decode<T, Decoder>(_ type: T.Type, using decoder: Decoder) throws where T : Decodable, Decoder : TopLevelDecoder
```

#### Discussion

> **Note**: `ColumnDecodingError` if an element fails to decode.

## Parameters

- `type`: The type of the value to decode.
- `decoder`: A decoder that accepts the column elements’ type.

## See Also

- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> AnyColumn](anycolumn/decoded(_:using:).md)
  Decodes data for each element of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/decode(_:using:))*