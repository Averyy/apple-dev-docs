# randomSplitBySequence(proportion:by:on:seed:)

**Framework**: Create ML  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func randomSplitBySequence(proportion: Double, by sequenceIdentifierColumn: String, on column: String, seed: Int = 1) -> (MLDataTable, remaining: MLDataTable)
```

## See Also

- [func stratifiedSplit<RNG>(proportions: [Double], on: String, generator: inout RNG) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:generator:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplit(proportions: [Double], on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:seed:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplitBySequence<RNG>(proportions: [Double], by: String, on: String, generator: inout RNG) throws -> MLDataTable](mldatatable/stratifiedsplitbysequence(proportions:by:on:generator:).md)
  Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.
- [func stratifiedSplitBySequence(proportions: [Double], by: String, on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplitbysequence(proportions:by:on:seed:).md)
  Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/randomsplitbysequence(proportion:by:on:seed:))*