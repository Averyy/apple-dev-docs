# encoded(_:using:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a column by encoding each element’s value.

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
func encoded<T, Encoder>(_ type: T.Type, using encoder: Encoder) throws -> AnyColumn where T : Encodable, Encoder : TopLevelEncoder
```

## Return Value

A new column of encoded values.

## Discussion

> **Throws**: `ColumnEncodingError` when the encoder fails to encode an element.

## Parameters

- `type`: The column underlying type.
- `encoder`: An encoder.

## See Also

### Encoding a Column
- [func encode<T, Encoder>(T.Type, using: Encoder) throws](./encode%28_,using%29.md)
  Encodes each element of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/encoded(_:using:))*