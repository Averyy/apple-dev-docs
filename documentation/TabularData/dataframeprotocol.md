# DataFrameProtocol

**Framework**: TabularData  
**Kind**: protocol

A type that represents a data frame.

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
protocol DataFrameProtocol
```

## Topics

### Inspecting a Data Frame Type
- [var isEmpty: Bool](dataframeprotocol/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframeprotocol/shape.md)
  The number or rows and columns of the data frame type.
- [var columns: [Self.ColumnType]](dataframeprotocol/columns.md)
  The columns of the underlying data frame.
- [associatedtype ColumnType : AnyColumnProtocol](dataframeprotocol/columntype.md)
  A type that conforms to the type-erased column protocol.
- [var rows: DataFrame.Rows](dataframeprotocol/rows.md)
  The rows of the underlying data frame.
- [DataFrame.Rows](dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](dataframeprotocol/base.md)
  The underlying data frame.
### Accessing Rows
- [subscript(Range<Int>) -> DataFrame.Slice](dataframeprotocol/subscript(_:).md)
  Accesses a slice of the data frame type with an index range.
- [subscript<R>(R) -> DataFrame.Slice](dataframeprotocol/subscript(_:)-8hly3.md)
  Accesses rows of a data frame type with an index range expression.
### Creating Two Slices by Splitting Rows
- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](dataframeprotocol/randomsplit(by:seed:).md)
  Generates two data frame slices by randomly splitting the rows of the data table.
- [func randomSplit<G>(by: Double, using: inout G) -> (DataFrame.Slice, DataFrame.Slice)](dataframeprotocol/randomsplit(by:using:).md)
  Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.
### Creating Two Data Frames by Splitting Rows
- [func stratifiedSplit(on: String, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-9iauf.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.
- [func stratifiedSplit(on: String..., by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-8szu1.md)
  Generates two data frames by randomly splitting the rows of multiple columns, which you select by their names, into strata.
- [func stratifiedSplit<T>(on: ColumnID<T>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-714jk.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by column identifier, into strata.
- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.
- [func stratifiedSplit<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:_:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.
### Creating a Data Frame by Sorting a Column
- [func sorted(on: String, order: Order) -> DataFrame](dataframeprotocol/sorted(on:order:)-818u5.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframeprotocol/sorted(on:_:order:)-8d7rr.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframeprotocol/sorted(on:_:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: ColumnID<T>, order: Order) -> DataFrame](dataframeprotocol/sorted(on:order:)-5nl5c.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframeprotocol/sorted(on:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.
### Creating a Data Frame by Sorting Multiple Columns
- [func sorted<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, order: Order) -> DataFrame](dataframeprotocol/sorted(on:_:order:)-79los.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to two columns that you select by their column identifiers.
- [func sorted<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order) -> DataFrame](dataframeprotocol/sorted(on:_:_:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to three columns that you select by their column identifiers.
### Creating a Data Frame by Joining Another Data Frame
- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-1gp6k.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-7u2tw.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-9629e.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-mvic.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.
- [enum JoinKind](joinkind.md)
  An operation type that joins two data frame types.
### Creating a Row Grouping by a Column
- [func grouped<GroupingKey>(by: ColumnID<GroupingKey>) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:)-77mq2.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframeprotocol/grouped(by:timeunit:)-7s782.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframeprotocol/grouped(by:timeunit:)-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:transform:)-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframeprotocol/grouped(by:transform:)-3aade.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
### Creating a Row Grouping by Multiple Columns
- [func grouped(by: String...) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:)-4wcw6.md)
  Creates a grouping from multiple columns you select by name.
- [func grouped<T>(by: ColumnID<T>...) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:)-6m6to.md)
  Creates a grouping from multiple columns that you select by column identifier.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframeprotocol/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
### Saving a Data Frame Type to a CSV Format
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframeprotocol/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframeprotocol/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.
### Describing a Data Frame Type
- [func description(options: FormattingOptions) -> String](dataframeprotocol/description(options:).md)
  Generates a text representation of the data frame type.
### Instance Methods
- [func jsonRepresentation(options: JSONWritingOptions) throws -> Data](dataframeprotocol/jsonrepresentation(options:).md)
  Generates a JSON data instance of the data frame.
- [func writeJSON(to: URL, options: JSONWritingOptions) throws](dataframeprotocol/writejson(to:options:).md)
  Creates a JSON file with the contents of the data frame.

## Relationships

### Conforming Types
- [DataFrame](dataframe.md)
- [DataFrame.Slice](dataframe/slice.md)

## See Also

- [struct DataFrame](dataframe.md)
  A collection that arranges data in rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol)*