# append(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds the rows of a slice from a data frame.

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
mutating func append(_ other: DataFrame.Slice)
```

## Discussion

The method ignores columns in `other` that don’t exist in the data frame. The method fills the values for columns in the data frame that don’t exist in `other` to `nil`.

## Parameters

- `other`: A slice of a data frame. The columns in `other` that have the same name as columns in the data frame must also have the same type.

## See Also

### Adding multiple rows from a data frame
- [func append(DataFrame)](./append%28_%29-36sor.md)
  Adds the rows of another data frame.
- [func append(rowsOf: DataFrame)](./append%28rowsof%29.md)
  Adds the rows of another data frame that has the same column names and types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/append(_:)-5l4c5)*