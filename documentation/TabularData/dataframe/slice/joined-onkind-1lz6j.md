# joined(_:on:kind:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by joining with another data frame type with a common column that you select by identifier.

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
func joined<R, T>(_ other: R, on columnID: ColumnID<T>, kind: JoinKind = .inner) -> DataFrame where R : DataFrameProtocol, T : Hashable
```

#### Return Value

A new data frame.

## Parameters

- `other`: A data frame type that represents the right side of the join.
- `columnID`: A column identifier that exists in both data frame types.
- `kind`: A join operation type.

## See Also

- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-2glok.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1misl.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-3zgye.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/joined(_:on:kind:)-1lz6j)*