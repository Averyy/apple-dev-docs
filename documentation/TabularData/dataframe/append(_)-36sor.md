# append(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds the rows of another data frame.

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
mutating func append(_ other: DataFrame)
```

## Discussion

The method ignores columns in `other` that don’t exist in the data frame. It fills the values for columns in the data frame that don’t exist in `other` to `nil`. It raises a fatal error if columns with the same name have different types. The following code shows how to check that the columns match.

```
func columnTypesAreEqual(_ left: DataFrame, _ right: DataFrame) -> Bool {
    for rightColumn in right.columns {
        guard let index = left.indexOfColumn(rightColumn.name) else {
            continue
        }
        let leftColumn = left.columns[index]
        if leftColumn.wrappedElementType != rightColumn.wrappedElementType {
            return false
        }
    }
    return true
}
```

## Parameters

- `other`: Another data frame. The columns in `other` that have the same name as columns in the data frame must also have the same type.

## See Also

### Adding multiple rows from a data frame
- [func append(rowsOf: DataFrame)](./append%28rowsof%29.md)
  Adds the rows of another data frame that has the same column names and types.
- [func append(DataFrame.Slice)](./append%28_%29-5l4c5.md)
  Adds the rows of a slice from a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/append(_:)-36sor)*