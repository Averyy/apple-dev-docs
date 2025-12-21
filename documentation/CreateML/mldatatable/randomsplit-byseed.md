# randomSplit(by:seed:)

**Framework**: Create ML  
**Kind**: method

Creates two mutually exclusive, randomly divided subsets of the table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func randomSplit(by proportion: Double, seed: Int = 1) -> (MLDataTable, MLDataTable)
```

## Mentions

- [Creating a word tagger model](creating-a-word-tagger-model.md)

#### Return Value

Two new data tables.

## Parameters

- `proportion`: A value between   and   indicating the fraction of   rows to go into one subset. The remaining rows go into the other subset.
- `seed`: A random number generator seed. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/randomsplit(by:seed:))*