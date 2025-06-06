# group(columnsNamed:aggregators:)

**Framework**: Create ML  
**Kind**: method

Creates a new data table with the given columns and adds a new column for each of the given aggregators.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func group<S>(columnsNamed: String..., aggregators: S) -> MLDataTable where S : Sequence, S.Element == MLDataTable.Aggregator
```

#### Return Value

A new data table.

#### Discussion

- columnsNamed: The name of the columns to include in the new data table.
- aggregators: A sequence of aggregators, each of which adds a column in the new data table.

## See Also

- [MLDataTable.Aggregator](mldatatable/aggregator.md)
  A collection of column operations you can use with a data table’s `group` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/group(columnsnamed:aggregators:))*