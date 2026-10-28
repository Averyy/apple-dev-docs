# sorted(on:order:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.

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
func sorted(on columnName: String, order: Order = .ascending) -> DataFrame
```

## Discussion

This is a convenience method that only works for columns of the following types:

- [`Bool`](../../Swift/bool.md)
- [`Int`](../../Swift/int.md)
- [`Float`](../../Swift/float.md)
- [`Double`](../../Swift/double.md)
- [`Date`](../../Foundation/date.md)

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnName`: The name of a column.
- `order`: A sorting order.

## See Also

### Creating a Data Frame by Sorting a Column
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](./sorted%28on,_,order%29-8d7rr.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](./sorted%28on,_,by%29.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: ColumnID<T>, order: Order) -> DataFrame](./sorted%28on,order%29-5nl5c.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](./sorted%28on,by%29.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/sorted(on:order:)-818u5)*