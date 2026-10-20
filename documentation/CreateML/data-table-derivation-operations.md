# Data table derivation operations

**Framework**: Create ML  
**Role**: API Collection

Create new data tables by manipulating an existing data table.

#### Overview

Use these methods to preprocess your data programmatically in Create ML before training a model. For example, you can create a data table by merging two data tables, fill in missing values, and then discarding duplicate rows.

All of these methods create new data tables, leaving the original data table unmodified.

## Topics

### Aggregating rows
- [func group<S>(columnsNamed: String..., aggregators: S) -> MLDataTable](./mldatatable/group%28columnsnamed,aggregators%29.md)
  Creates a new data table with the given columns and adds a new column for each of the given aggregators.
- [MLDataTable.Aggregator](./mldatatable/aggregator.md)
  A collection of column operations you can use with a data table’s `group` method.
### Sorting rows
- [func sort(columnNamed: String, byIncreasingOrder: Bool) -> MLDataTable](./mldatatable/sort%28columnnamed,byincreasingorder%29.md)
  Creates a new data table by sorting the table by the given column.
### Splitting a data table
- [func randomSplit(by: Double, seed: Int) -> (MLDataTable, MLDataTable)](./mldatatable/randomsplit%28by,seed%29.md)
  Creates two mutually exclusive, randomly divided subsets of the table.
### Merging data tables
- [func join(with: MLDataTable, on: String..., type: MLDataTable.JoinType) -> MLDataTable](./mldatatable/join%28with,on,type%29.md)
  Creates a new data table by merging two data tables by the given columns.
- [MLDataTable.JoinType](./mldatatable/jointype.md)
  Join types available for [`MLDataTable`](./mldatatable.md) join operations.
### Filling in missing values
- [func fillMissing(columnNamed: String, with: MLDataValue) -> MLDataTable](./mldatatable/fillmissing%28columnnamed,with%29.md)
  Creates a modified copy of the table by filling in the missing values in the named column.
### Masking rows
- [subscript(MLDataColumn<Bool>) -> MLDataTable](./mldatatable/subscript%28_%29-3opgl.md)
  Creates a subset of the table by masking the rows with the given column of Booleans.
- [subscript(MLUntypedColumn) -> MLDataTable](./mldatatable/subscript%28_%29-10r4l.md)
  Creates a subset of the table by masking the rows with the given untyped column.
### Discarding rows
- [func dropMissing() -> MLDataTable](./mldatatable/dropmissing%28%29.md)
  Creates a subset of the table by removing any row missing one or more values.
- [func dropDuplicates() -> MLDataTable](./mldatatable/dropduplicates%28%29.md)
  Creates a subset of the table by removing all duplicate rows.
- [func exclude<T>(T..., of: String) -> MLDataTable](./mldatatable/exclude%28_,of%29.md)
  Creates a subset of the table by excluding the rows that contain any of the given values in the given column.
- [func randomSample(by: Double, seed: Int) -> MLDataTable](./mldatatable/randomsample%28by,seed%29.md)
  Creates a subset of the table by randomly selecting the given proportion of rows.
### Selecting rows
- [subscript(Range<Int>) -> MLDataTable](./mldatatable/subscript%28_%29-7h4j3.md)
  Creates a subset of the table given a range of rows.
- [subscript<R>(R) -> MLDataTable](./mldatatable/subscript%28_%29-5le8a.md)
  Creates a subset of the table given a range expression of rows.
- [func prefix(Int) -> MLDataTable](./mldatatable/prefix%28_%29.md)
  Creates a subset of the table given a number of initial rows.
- [func suffix(Int) -> MLDataTable](./mldatatable/suffix%28_%29.md)
  Creates a subset of the table given a number of final rows.
- [func intersect<T>(T..., of: String) -> MLDataTable](./mldatatable/intersect%28_,of%29.md)
  Creates a subset of the table by including the rows that contain any of the given values in the given column.
### Selecting columns
- [subscript<S>(S) -> MLDataTable](./mldatatable/subscript%28_%29-2wkan.md)
  Creates a subset of the table given a sequence of column names.
### Compacting rows
- [func condense(columnNamed: String, to: String) -> MLDataTable](./mldatatable/condense%28columnnamed,to%29.md)
  Creates a new data table where duplicate row values in the given column are condensed into a new sequence-type column.
### Expanding rows
- [func expand(columnNamed: String, to: String) -> MLDataTable](./mldatatable/expand%28columnnamed,to%29.md)
  Creates a new data table where duplicate row values in the given column are condensed into a new sequence-type column.
### Compacting columns
- [func pack(columnsNamed: String..., to: String, type: MLDataTable.PackType, filling: MLDataValue) -> MLDataTable](./mldatatable/pack%28columnsnamed,to,type,filling%29.md)
  Creates a new data table with an additional column that contains the combined values of the given columns.
- [MLDataTable.PackType](./mldatatable/packtype.md)
  The storage operations for combining multiple columns into one.
### Expanding columns
- [func unpack(columnNamed: String, valueTypes: [MLDataValue.ValueType]?, indexSubset: [Int]?, keySubset: [String]?) -> MLDataTable](./mldatatable/unpack%28columnnamed,valuetypes,indexsubset,keysubset%29.md)
  Creates a new data table with additional columns that contain the unpacked collections in the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/data-table-derivation-operations)*