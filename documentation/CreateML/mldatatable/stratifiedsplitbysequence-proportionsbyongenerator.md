# stratifiedSplitBySequence(proportions:by:on:generator:)

**Framework**: Create ML  
**Kind**: method

Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplitBySequence<RNG>(proportions: [Double], by sequenceIdentifierColumn: String, on column: String, generator: inout RNG) throws -> MLDataTable where RNG : RandomNumberGenerator
```

#### Return Value

A new MLDataTable with an additional partition column with the index of the partition for each row.

#### Discussion

The proportions specified will be applied uniformly to each label being partitioned on.

## Parameters

- `proportions`: An array of values on [0,1] specifying the proprtions in each partition. Automatically normalized to 1.
- `sequenceIdentifierColumn`: The sequence identifier column in an MLDataTable to identify rows of a sequence.
- `column`: The column in an MLDataTable being stratified on.
- `generator`: User-defined RandomNumberGenerator to use in stratification.

## See Also

- [func randomSplitBySequence(proportion: Double, by: String, on: String, seed: Int) -> (MLDataTable, remaining: MLDataTable)](mldatatable/randomsplitbysequence(proportion:by:on:seed:).md)
- [func stratifiedSplit<RNG>(proportions: [Double], on: String, generator: inout RNG) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:generator:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplit(proportions: [Double], on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:seed:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplitBySequence(proportions: [Double], by: String, on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplitbysequence(proportions:by:on:seed:).md)
  Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/stratifiedsplitbysequence(proportions:by:on:generator:))*