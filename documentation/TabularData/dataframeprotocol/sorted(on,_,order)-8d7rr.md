# sorted(on:_:order:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.

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
func sorted<T>(on columnName: String, _ type: T.Type, order: Order = .ascending) -> DataFrame where T : Comparable
```

#### Discussion

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnName`: The name of a column.
- `type`: The column’s type.
- `order`: A sorting order.

## See Also

### Creating a Data Frame by Sorting a Column
- [func sorted(on: String, order: Order) -> DataFrame](./sorted%28on,order%29-818u5.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](./sorted%28on,_,by%29.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: ColumnID<T>, order: Order) -> DataFrame](./sorted%28on,order%29-5nl5c.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](./sorted%28on,by%29.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/sorted(on:_:order:)-8d7rr)*