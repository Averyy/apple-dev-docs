# counts()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.

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
func counts() -> DataFrame
```

## Discussion

The name of the data frame’s column that stores the number of rows in each group is *count*.

## See Also

### Aggregating a Row Grouping
- [func counts(order: Order?) -> DataFrame](./counts%28order%29.md)
  Generates a data frame, that you choose how to sort, with two columns, one that has a row for each group key and another for the number or rows in the group.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](./sums%28_,_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](./sums%28_,order%29.md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](./means%28_,_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](./means%28_,order%29.md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](./minimums%28_,_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](./minimums%28_,order%29.md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](./maximums%28_,_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](./maximums%28_,order%29.md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](./aggregated%28on,into,transform%29.md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: [String], naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](./aggregated%28on,naming,transform%29.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/counts())*