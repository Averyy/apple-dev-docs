# joined(_:on:kind:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.

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
func joined<R>(_ other: R, on columnNames: (left: String, right: String), kind: JoinKind = .inner) -> DataFrame where R : DataFrameProtocol
```

#### Return Value

A new data frame.

## Parameters

- `other`: A data frame type that represents the right side of the join.
- `columnNames`: The column names of the data frame and the other data frame type,  , respectively.
- `kind`: A join operation type.

## See Also

- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-2glok.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-3zgye.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1lz6j.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/joined(_:on:kind:)-1misl)*