# addAlias(_:forColumn:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds an alternative name for a column.

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
mutating func addAlias(_ alias: String, forColumn columnName: String)
```

## Parameters

- `alias`: An additional name for the column.
- `columnName`: The name of a column.

## See Also

### Aliasing a column name
- [func columnNames(forAlias: String) -> [String]](./columnnames%28foralias%29.md)
  Returns the column names for an alias.
- [func removeAlias(String)](./removealias%28_%29.md)
  Removes an alternative name for a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/addalias(_:forcolumn:))*