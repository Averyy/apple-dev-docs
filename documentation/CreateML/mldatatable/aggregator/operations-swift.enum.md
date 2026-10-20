# MLDataTable.Aggregator.Operations

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The operations that an aggregator can perform on a column in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Operations
```

## Topics

### Aggregation operations
- [MLDataTable.Aggregator.Operations.min](./operations-swift.enum/min.md)
  An operation that identifies the smallest value in a column.
- [MLDataTable.Aggregator.Operations.max](./operations-swift.enum/max.md)
  An operation that identifies the largest value in a column.
- [MLDataTable.Aggregator.Operations.sum](./operations-swift.enum/sum.md)
  An operation that the adds the values in a column.
- [MLDataTable.Aggregator.Operations.mean](./operations-swift.enum/mean.md)
  An operation that computes the mean of the values in a column.
- [MLDataTable.Aggregator.Operations.stdev](./operations-swift.enum/stdev.md)
  An operation that computes the standard deviation of the values in a column.
- [MLDataTable.Aggregator.Operations.variance](./operations-swift.enum/variance.md)
  An operation that computes the variance in a column.
- [MLDataTable.Aggregator.Operations.count](./operations-swift.enum/count.md)
  An operation that counts the number of values in a column.
- [MLDataTable.Aggregator.Operations.distinctCount](./operations-swift.enum/distinctcount.md)
  An operation that counts the number of distinct values in a column.
- [MLDataTable.Aggregator.Operations.randomlySelectOne](./operations-swift.enum/randomlyselectone.md)
  An operation that selects a random value from a column.
- [MLDataTable.Aggregator.Operations.sequenceMerge](./operations-swift.enum/sequencemerge.md)
  An operation that combines the values in a column into a sequence.
- [MLDataTable.Aggregator.Operations.dictionaryMerge(valueColumn:)](./operations-swift.enum/dictionarymerge%28valuecolumn%29.md)
  An operation that combines two columns into a dictionary, using the given column as the values for that dictionary.
- [MLDataTable.Aggregator.Operations.argmin(outputColumn:)](./operations-swift.enum/argmin%28outputcolumn%29.md)
  An operation that retrieves the value in the given column that’s in the same row as the minimum value of the aggregator’s column.
- [MLDataTable.Aggregator.Operations.argmax(outputColumn:)](./operations-swift.enum/argmax%28outputcolumn%29.md)
  An operation that retrieves the value in the given column that’s in the same row as the maximum value of the aggregator’s column.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring an aggregator
- [var columnName: String](./columnname.md)
  The name of the column on which the aggregator performs operations on.
- [var operations: [MLDataTable.Aggregator.Operations]](./operations-swift.property.md)
  An array of operations to perform on a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/aggregator/operations-swift.enum)*