# SummaryColumnIDs

**Framework**: TabularData  
**Kind**: enum  
**Role**: Enumeration

The summary data frame column identifiers.

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
enum SummaryColumnIDs
```

## Topics

### Type Properties
- [static let columnName: ColumnID<String>](./summarycolumnids/columnname.md)
  The identifier that represents the summary’s column that contains the column names in a data frame.
- [static let firstQuartile: ColumnID<Double>](./summarycolumnids/firstquartile.md)
  The identifier that represents the summary’s column of first quartiles.
- [static let maximum: ColumnID<Double>](./summarycolumnids/maximum.md)
  The identifier that represents the summary’s column of maximums.
- [static let mean: ColumnID<Double>](./summarycolumnids/mean.md)
  The identifier that represents the summary’s column of arithmetic means.
- [static let median: ColumnID<Double>](./summarycolumnids/median.md)
  The identifier that represents the summary’s column of medians.
- [static let minimum: ColumnID<Double>](./summarycolumnids/minimum.md)
  The identifier that represents the summary’s column of minimums.
- [static let mode: ColumnID<[Any]>](./summarycolumnids/mode.md)
  The identifier that represents the summary’s column of most frequent elements.
- [static let noneCount: ColumnID<Int>](./summarycolumnids/nonecount.md)
  The identifier that represents the summary’s column of missing counts.
- [static let someCount: ColumnID<Int>](./summarycolumnids/somecount.md)
  The identifier that represents the summary’s column of non-missing counts.
- [static let standardDeviation: ColumnID<Double>](./summarycolumnids/standarddeviation.md)
  The identifier that represents the summary’s column of standard deviations.
- [static let thirdQuartile: ColumnID<Double>](./summarycolumnids/thirdquartile.md)
  The identifier that represents the summary’s column of third quartiles.
- [static let uniqueCount: ColumnID<Int>](./summarycolumnids/uniquecount.md)
  The identifier that represents the summary’s column of unique counts.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Summarizing a Data Frame
- [func summary() -> DataFrame](./dataframe/summary%28%29.md)
  Generates a data frame that summarizes the columns of the data frame.
- [func summary(of: String...) -> DataFrame](./dataframe/summary%28of%29.md)
  Generates a data frame that summarizes the columns you select by name.
- [func summary(ofColumns: Int...) -> DataFrame](./dataframe/summary%28ofcolumns%29.md)
  Generates a data frame that summarizes the columns you select by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/summarycolumnids)*