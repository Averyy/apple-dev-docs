# encodeColumn(_:_:using:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Encodes the elements of a column you select by name.

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
mutating func encodeColumn<T, Encoder>(_ columnName: String, _ type: T.Type, using encoder: Encoder) throws where T : Encodable, Encoder : TopLevelEncoder
```

## Discussion

> **Throws**: `ColumnEncodingError` when the encoder fails to encode a column element.

## Parameters

- `columnName`: The name of a column.
- `type`: The type of the column.
- `encoder`: A encoder that accepts the column’s type.

## See Also

### Encoding a column
- [func encodeColumn<T, Encoder>(ColumnID<T>, using: Encoder) throws](./encodecolumn%28_,using%29.md)
  Encodes the elements of a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/encodecolumn(_:_:using:))*