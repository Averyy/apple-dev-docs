# append(row:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds a comma-separated, or variadic, list of values as a row to the data frame.

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
mutating func append(row: Any?...)
```

## Parameters

- `row`: A comma-separated, or variadic, list of optional values. Each value’s type must match the type of the corresponding column in the data frame.

## See Also

### Adding a row
- [func appendEmptyRow()](./appendemptyrow%28%29.md)
  Adds an empty row to the data frame.
- [func append(valuesByColumn: [String : Any?])](./append%28valuesbycolumn%29.md)
  Adds a dictionary’s values as a row to the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/append(row:)-3p6lx)*