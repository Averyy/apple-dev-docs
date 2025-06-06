# decoded(_:using:)

**Framework**: TabularData  
**Kind**: method

Generates a column by decoding each element’s data.

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
func decoded<T, Decoder>(_ type: T.Type, using decoder: Decoder) throws -> Column<T> where WrappedElement == Decoder.Input, T : Decodable, Decoder : TopLevelDecoder
```

#### Return Value

A new column of decoded values.

#### Discussion

> **Note**: `ColumnDecodingError` when the decoder fails to decode an element.

`ColumnDecodingError` when the decoder fails to decode an element.

## Parameters

- `type`: The decodable value’s type.
- `decoder`: A decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/decoded(_:using:))*