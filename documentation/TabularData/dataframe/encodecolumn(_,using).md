# encodeColumn(_:using:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Encodes the elements of a column you select by column identifier.

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
mutating func encodeColumn<T, Encoder>(_ id: ColumnID<T>, using encoder: Encoder) throws where T : Encodable, Encoder : TopLevelEncoder
```

## Discussion

> **Throws**: `ColumnEncodingError` when the encoder fails to encode a column element.

## Parameters

- `id`: The name of a column.
- `encoder`: A encoder that accepts the column’s type.

## See Also

### Encoding a column
- [func encodeColumn<T, Encoder>(String, T.Type, using: Encoder) throws](./encodecolumn%28_,_,using%29.md)
  Encodes the elements of a column you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/encodecolumn(_:using:))*