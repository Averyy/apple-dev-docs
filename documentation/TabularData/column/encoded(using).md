# encoded(using:)

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
func encoded<Encoder>(using encoder: Encoder) throws -> Column<Encoder.Output> where Encoder : TopLevelEncoder
```

Available when `WrappedElement` conforms to `Encodable`.

## Return Value

A new column of encoded values.

## Discussion

> **Throws**: `ColumnEncodingError` when the encoder fails to encode an element.

## Parameters

- `encoder`: An encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/encoded(using:))*