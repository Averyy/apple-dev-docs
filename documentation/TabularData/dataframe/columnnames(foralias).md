# columnNames(forAlias:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns the column names for an alias.

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
func columnNames(forAlias alias: String) -> [String]
```

## Discussion

Use this method to discover whether an alias refers to more than one column. For example, a data frame may have multiple columns with the same name after you call its [`joined(_:on:kind:)`](../dataframeprotocol/joined%28_,on,kind%29-1gp6k.md) method.

## See Also

### Aliasing a column name
- [func addAlias(String, forColumn: String)](./addalias%28_,forcolumn%29.md)
  Adds an alternative name for a column.
- [func removeAlias(String)](./removealias%28_%29.md)
  Removes an alternative name for a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/columnnames(foralias:))*