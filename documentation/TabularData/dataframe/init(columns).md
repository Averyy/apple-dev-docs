# init(columns:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a new data frame from a sequence of columns.

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
init<S>(columns: S) where S : Sequence, S.Element == AnyColumn
```

## Parameters

- `columns`: A sequence of type-erased columns.

## See Also

### Creating a Data Frame
- [init()](./init%28%29.md)
  Creates an empty data frame with no rows or columns.
- [init(dictionaryLiteral: (String, [Any?])...)](./init%28dictionaryliteral%29.md)
  Creates a data frame from a dictionary literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(columns:))*