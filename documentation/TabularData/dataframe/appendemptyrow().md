# appendEmptyRow()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds an empty row to the data frame.

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
mutating func appendEmptyRow()
```

## Discussion

Each value in an empty row is `nil`.

## See Also

### Adding a row
- [func append(row: Any?...)](./append%28row%29-3p6lx.md)
  Adds a comma-separated, or variadic, list of values as a row to the data frame.
- [func append(valuesByColumn: [String : Any?])](./append%28valuesbycolumn%29.md)
  Adds a dictionary’s values as a row to the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/appendemptyrow())*