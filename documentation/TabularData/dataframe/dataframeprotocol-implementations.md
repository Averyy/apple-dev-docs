# DataFrameProtocol Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var base: DataFrame](dataframe/base.md)
  The underlying data frame.
- [var isEmpty: Bool](dataframe/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
### Instance Methods
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.
- [func description(options: FormattingOptions) -> String](dataframe/description(options:).md)
  Generates a text representation of the data frame type.
- [func grouped<GroupingKey>(by: ColumnID<GroupingKey>) -> RowGrouping<GroupingKey>](dataframe/grouped(by:)-2hm43.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped(by: String...) -> some RowGroupingProtocol](dataframe/grouped(by:)-96zo8.md)
  Creates a grouping from multiple columns you select by name.
- [func grouped<T>(by: ColumnID<T>...) -> some RowGroupingProtocol](dataframe/grouped(by:)-qniy.md)
  Creates a grouping from multiple columns that you select by column identifier.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/grouped(by:timeunit:)-538ya.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/grouped(by:timeunit:)-huz4.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-11u79.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/grouped(by:transform:)-4jlj3.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframe/joined(_:on:kind:)-5mpnt.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframe/joined(_:on:kind:)-6moa8.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframe/joined(_:on:kind:)-8v4sp.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframe/joined(_:on:kind:)-969k1.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.
- [func jsonRepresentation(options: JSONWritingOptions) throws -> Data](dataframe/jsonrepresentation(options:).md)
  Generates a JSON data instance of the data frame.
- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/randomsplit(by:seed:).md)
  Generates two data frame slices by randomly splitting the rows of the data table.
- [func randomSplit<G>(by: Double, using: inout G) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/randomsplit(by:using:).md)
  Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.
- [func sorted<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order) -> DataFrame](dataframe/sorted(on:_:_:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to three columns that you select by their column identifiers.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/sorted(on:_:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframe/sorted(on:_:order:)-7gt7j.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, order: Order) -> DataFrame](dataframe/sorted(on:_:order:)-90o0t.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to two columns that you select by their column identifiers.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/sorted(on:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.
- [func sorted<T>(on: ColumnID<T>, order: Order) -> DataFrame](dataframe/sorted(on:order:)-6kn10.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier.
- [func sorted(on: String, order: Order) -> DataFrame](dataframe/sorted(on:order:)-6o09e.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func stratifiedSplit<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/stratifiedsplit(on:_:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.
- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.
- [func stratifiedSplit(on: String..., by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/stratifiedsplit(on:by:randomseed:)-1x8p6.md)
  Generates two data frames by randomly splitting the rows of multiple columns, which you select by their names, into strata.
- [func stratifiedSplit(on: String, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/stratifiedsplit(on:by:randomseed:)-50zwv.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.
- [func stratifiedSplit<T>(on: ColumnID<T>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/stratifiedsplit(on:by:randomseed:)-7e5pd.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by column identifier, into strata.
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframe/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func writeJSON(to: URL, options: JSONWritingOptions) throws](dataframe/writejson(to:options:).md)
  Creates a JSON file with the contents of the data frame.
### Subscripts
- [subscript<R>(R) -> DataFrame.Slice](dataframe/subscript(_:)-4rx4a.md)
  Accesses rows of a data frame type with an index range expression.
- [subscript(Range<Int>) -> DataFrame.Slice](dataframe/subscript(_:)-8wcl1.md)
  Accesses a slice of the data frame type with an index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/dataframeprotocol-implementations)*