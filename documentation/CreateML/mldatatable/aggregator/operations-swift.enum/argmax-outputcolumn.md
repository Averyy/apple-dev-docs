# MLDataTable.Aggregator.Operations.argmax(outputColumn:)

**Framework**: Create ML  
**Kind**: case

An operation that retrieves the value in the given column that’s in the same row as the maximum value of the aggregator’s column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case argmax(outputColumn: String)
```

#### Discussion

Use this operation to find a value in the given `outputColumn` that’s in the same row as the maximum value in the aggregator’s column. For example, take the following data table of drink ratings.

```swift
let teaVsCoffee = try! MLDataTable(dictionary: [
    "userName" : ["Sara", "Sara", "James", "James"],
    "drink"    : ["tea", "coffee", "tea", "coffee"],
    "rating"   : [5.0, 3.5, 3.1, 4.9]
])

print(teaVsCoffee)

Prints ...
 Columns:
    ratingfloat
    drinkstring
    userNamestring
Rows: 4 Data:
+----------------+----------------+----------------+
| drink          | userName       | rating         |
+----------------+----------------+----------------+
| tea            | Sara           | 5              |
| coffee         | Sara           | 3.5            |
| tea            | James          | 3.1            |
| coffee         | James          | 4.9            |
+----------------+----------------+----------------+
[4 rows x 3 columns]
```

To find out which person gave the highest rating for any particular beverage, use the `argmax` operation with the `"userName"` string. Then use the [`group(columnsNamed:aggregators:)`](mldatatable/group(columnsnamed:aggregators:).md) function group the `"drink"` column.

```swift
var highestRater = MLDataTable.Aggregator(operations: .argmax(outputColumn: "userName"),
                                          of: "rating")

let highestDrinkRatings = teaVsCoffee.group(columnsNamed: "drink",
                                            aggregators: [highestRater])
print(highestDrinkRatings)

Prints ...
+----------------+----------------+
| drink          | ratingArgmax   |
+----------------+----------------+
| tea            | Sara           |
| coffee         | James          |
+----------------+----------------+
[2 rows x 2 columns]
```

In this example, the drinks column only has two distinct drinks, tea and coffee, which result in a data table with two rows.

- outputColumn: The name of the column that holds the values associated with the maximum values of the aggregator’s designated column.

## See Also

- [MLDataTable.Aggregator.Operations.min](mldatatable/aggregator/operations-swift.enum/min.md)
  An operation that identifies the smallest value in a column.
- [MLDataTable.Aggregator.Operations.max](mldatatable/aggregator/operations-swift.enum/max.md)
  An operation that identifies the largest value in a column.
- [MLDataTable.Aggregator.Operations.sum](mldatatable/aggregator/operations-swift.enum/sum.md)
  An operation that the adds the values in a column.
- [MLDataTable.Aggregator.Operations.mean](mldatatable/aggregator/operations-swift.enum/mean.md)
  An operation that computes the mean of the values in a column.
- [MLDataTable.Aggregator.Operations.stdev](mldatatable/aggregator/operations-swift.enum/stdev.md)
  An operation that computes the standard deviation of the values in a column.
- [MLDataTable.Aggregator.Operations.variance](mldatatable/aggregator/operations-swift.enum/variance.md)
  An operation that computes the variance in a column.
- [MLDataTable.Aggregator.Operations.count](mldatatable/aggregator/operations-swift.enum/count.md)
  An operation that counts the number of values in a column.
- [MLDataTable.Aggregator.Operations.distinctCount](mldatatable/aggregator/operations-swift.enum/distinctcount.md)
  An operation that counts the number of distinct values in a column.
- [MLDataTable.Aggregator.Operations.randomlySelectOne](mldatatable/aggregator/operations-swift.enum/randomlyselectone.md)
  An operation that selects a random value from a column.
- [MLDataTable.Aggregator.Operations.sequenceMerge](mldatatable/aggregator/operations-swift.enum/sequencemerge.md)
  An operation that combines the values in a column into a sequence.
- [MLDataTable.Aggregator.Operations.dictionaryMerge(valueColumn:)](mldatatable/aggregator/operations-swift.enum/dictionarymerge(valuecolumn:).md)
  An operation that combines two columns into a dictionary, using the given column as the values for that dictionary.
- [MLDataTable.Aggregator.Operations.argmin(outputColumn:)](mldatatable/aggregator/operations-swift.enum/argmin(outputcolumn:).md)
  An operation that retrieves the value in the given column that’s in the same row as the minimum value of the aggregator’s column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/aggregator/operations-swift.enum/argmax(outputcolumn:))*