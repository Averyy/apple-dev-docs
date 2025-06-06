# RowGroupingProtocol Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func aggregated<Element, Result>(on: ColumnID<Element>, into: String?, transform: (DiscontiguousColumnSlice<Element>) throws -> Result) rethrows -> DataFrame](rowgrouping/aggregated(on:into:transform:).md)
  Generates a data frame with a column for the group identifier and a column of values from the transform.
- [func aggregated<Element, Result>(on: String..., naming: (String) -> String, transform: (DiscontiguousColumnSlice<Element>) throws -> Result?) rethrows -> DataFrame](rowgrouping/aggregated(on:naming:transform:)-6v6gq.md)
  Generates a data frame by aggregating each group’s contents for each column you select by name.
- [func counts() -> DataFrame](rowgrouping/counts.md)
  Generates a data frame with two columns, one that has a row for each group key and another for the number of rows in the group.
- [func maximums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/maximums(_:_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by name.
- [func maximums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/maximums(_:order:).md)
  Generates a data frame that contains the maximums of each group’s rows along a column you select by column identifier.
- [func means<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/means(_:_:order:).md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by name.
- [func means<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/means(_:order:).md)
  Generates a data frame that contains the average mean of each group’s rows along a column you select by column identifier.
- [func minimums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/minimums(_:_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by name.
- [func minimums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/minimums(_:order:).md)
  Generates a data frame that contains the minimums of each group’s rows along a column you select by column identifier.
- [func quantiles<N>(String, N.Type, quantile: N, order: Order?) -> DataFrame](rowgrouping/quantiles(_:_:quantile:order:).md)
  Generates a data frame that contains the quantile of each group’s rows along a column you select by name.
- [func quantiles<N>(ColumnID<N>, quantile: N, order: Order?) -> DataFrame](rowgrouping/quantiles(_:quantile:order:).md)
  Generates a data frame that contains the quantiles of each group’s rows along a column you select by column identifier.
- [func randomSplit(by: Double) -> (Self, Self)](rowgrouping/randomsplit(by:).md)
  Generates two row groupings by randomly splitting the original with a proportion.
- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](rowgrouping/randomsplit(by:seed:).md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.
- [func summary() -> any GroupSummaries](rowgrouping/summary.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](rowgrouping/summary(of:).md)
  Generates a group summaries instance for the columns you select by name.
- [func sums<N>(String, N.Type, order: Order?) -> DataFrame](rowgrouping/sums(_:_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by name.
- [func sums<N>(ColumnID<N>, order: Order?) -> DataFrame](rowgrouping/sums(_:order:).md)
  Generates a data frame that contains the sum of each group’s rows along a column you select by column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/rowgroupingprotocol-implementations)*