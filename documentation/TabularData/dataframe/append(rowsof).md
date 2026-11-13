# append(rowsOf:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds the rows of another data frame that has the same column names and types.

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
mutating func append(rowsOf other: DataFrame)
```

## Discussion

This method raises a fatal error if the data frame columns don’t match. The following code shows how to check that the columns match.

```
let sameColumns = left.columns.count == right.columns.count && zip(left.columns, right.columns).allSatisfy {
    $0.name == $1.name && $0.wrappedElementType == $1.wrappedElementType
}
```

## Parameters

- `other`: Another data frame that has the same number of columns. The columns in `other` must have the same names and types as the columns in the data frame.

## See Also

### Adding multiple rows from a data frame
- [func append(DataFrame)](./append%28_%29-36sor.md)
  Adds the rows of another data frame.
- [func append(DataFrame.Slice)](./append%28_%29-5l4c5.md)
  Adds the rows of a slice from a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/append(rowsof:))*