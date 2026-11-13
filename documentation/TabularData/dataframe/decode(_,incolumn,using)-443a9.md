# decode(_:inColumn:using:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Decodes the elements of a column you select by name.

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
mutating func decode<T, Decoder>(_ type: T.Type, inColumn columnName: String, using decoder: Decoder) throws where T : Decodable, Decoder : TopLevelDecoder
```

## Discussion

> **Throws**: `ColumnDecodingError` when the decoder fails to decode a column element.

## Parameters

- `type`: The type of the decodable value.
- `columnName`: The name of a column.
- `decoder`: A decoder that accepts the column’s type.

## See Also

### Decoding a column
- [func decode<T, Decoder>(T.Type, inColumn: ColumnID<Decoder.Input>, using: Decoder) throws](./decode%28_,incolumn,using%29-2brfw.md)
  Decodes the elements of a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/decode(_:incolumn:using:)-443a9)*