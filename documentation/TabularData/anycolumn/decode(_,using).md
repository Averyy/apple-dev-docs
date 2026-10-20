# decode(_:using:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

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

> **Throws**: `ColumnDecodingError` if an element fails to decode.

## Parameters

- `type`: The type of the value to decode.
- `decoder`: A decoder that accepts the column elements’ type.

## See Also

### Decoding a Column
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> AnyColumn](./decoded%28_,using%29.md)
  Decodes data for each element of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/decode(_:using:))*