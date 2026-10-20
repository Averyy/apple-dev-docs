# RowGroupingProtocol Implementations

**Framework**: TabularData  
**Role**: API Collection

## Topics

### Instance Methods
- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](./randomsplit%28by,seed%29.md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.
- [func summary() -> any GroupSummaries](./summary%28%29.md)
  Generates a group summaries instance for the columns of the row grouping.
- [func summary(of: [String]) -> any GroupSummaries](./summary%28of%29.md)
  Generates a group summaries instance for the columns you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/rowgroupingprotocol-implementations)*