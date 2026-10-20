# MLDataTable.Aggregator.Operations.max

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An operation that identifies the largest value in a column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case max
```

## See Also

### Aggregation operations
- [MLDataTable.Aggregator.Operations.min](./min.md)
  An operation that identifies the smallest value in a column.
- [MLDataTable.Aggregator.Operations.sum](./sum.md)
  An operation that the adds the values in a column.
- [MLDataTable.Aggregator.Operations.mean](./mean.md)
  An operation that computes the mean of the values in a column.
- [MLDataTable.Aggregator.Operations.stdev](./stdev.md)
  An operation that computes the standard deviation of the values in a column.
- [MLDataTable.Aggregator.Operations.variance](./variance.md)
  An operation that computes the variance in a column.
- [MLDataTable.Aggregator.Operations.count](./count.md)
  An operation that counts the number of values in a column.
- [MLDataTable.Aggregator.Operations.distinctCount](./distinctcount.md)
  An operation that counts the number of distinct values in a column.
- [MLDataTable.Aggregator.Operations.randomlySelectOne](./randomlyselectone.md)
  An operation that selects a random value from a column.
- [MLDataTable.Aggregator.Operations.sequenceMerge](./sequencemerge.md)
  An operation that combines the values in a column into a sequence.
- [MLDataTable.Aggregator.Operations.dictionaryMerge(valueColumn:)](./dictionarymerge%28valuecolumn%29.md)
  An operation that combines two columns into a dictionary, using the given column as the values for that dictionary.
- [MLDataTable.Aggregator.Operations.argmin(outputColumn:)](./argmin%28outputcolumn%29.md)
  An operation that retrieves the value in the given column that’s in the same row as the minimum value of the aggregator’s column.
- [MLDataTable.Aggregator.Operations.argmax(outputColumn:)](./argmax%28outputcolumn%29.md)
  An operation that retrieves the value in the given column that’s in the same row as the maximum value of the aggregator’s column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/aggregator/operations-swift.enum/max)*