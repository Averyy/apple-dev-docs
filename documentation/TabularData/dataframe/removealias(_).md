# removeAlias(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Removes an alternative name for a column.

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
mutating func removeAlias(_ alias: String)
```

## Parameters

- `alias`: An additional name for the column.

## See Also

### Aliasing a column name
- [func addAlias(String, forColumn: String)](./addalias%28_,forcolumn%29.md)
  Adds an alternative name for a column.
- [func columnNames(forAlias: String) -> [String]](./columnnames%28foralias%29.md)
  Returns the column names for an alias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/removealias(_:))*