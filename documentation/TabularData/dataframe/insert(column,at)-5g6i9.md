# insert(column:at:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Adds a typed column at a position in the data frame.

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
mutating func insert<T>(column: Column<T>, at index: Int)
```

## Discussion

The method inserts the new column before the column currently at `index`. If you pass the array’s `shape.columns` property as the `index` parameter, the method appends the new column to the data frame.

## Parameters

- `column`: A typed column. The column must have the same number of rows as the data frame, and must not have the same name as another column in the data frame.
- `index`: A column position in the data frame.

## See Also

### Adding a Column
- [func append(column: AnyColumn)](./append%28column%29-45s2v.md)
  Adds a type-erased column to the end of the data frame.
- [func append<T>(column: Column<T>)](./append%28column%29-aema.md)
  Adds a typed column to the end of the data frame.
- [func insert(column: AnyColumn, at: Int)](./insert%28column,at%29-784jb.md)
  Adds a type-erased column at a position in the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/insert(column:at:)-5g6i9)*