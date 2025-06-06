# DataFrameProtocol Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var isEmpty: Bool](dataframe/slice/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
### Instance Methods
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/slice/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.
- [func description(options: FormattingOptions) -> String](dataframe/slice/description(options:).md)
  Generates a text representation of the data frame type.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-13w3o.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-696t5.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/slice/grouped(by:transform:)-5eoog.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/slice/grouped(by:transform:)-7e9bm.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1lz6j.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1misl.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-2glok.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-3zgye.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func jsonRepresentation(options: JSONWritingOptions) throws -> Data](dataframe/slice/jsonrepresentation(options:).md)
  Generates a JSON data instance of the data frame.
- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/slice/randomsplit(by:seed:).md)
  Generates two data frame slices by randomly splitting the rows of the data table.
- [func randomSplit<G>(by: Double, using: inout G) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/slice/randomsplit(by:using:).md)
  Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.
- [func sorted<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:_:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to three columns that you select by their column identifiers.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/slice/sorted(on:_:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:order:)-37i2f.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:order:)-xr0h.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to two columns that you select by their column identifiers.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/slice/sorted(on:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.
- [func sorted(on: String, order: Order) -> DataFrame](dataframe/slice/sorted(on:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func stratifiedSplit<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.
- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.
- [func stratifiedSplit(on: String, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframe/slice/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func writeJSON(to: URL, options: JSONWritingOptions) throws](dataframe/slice/writejson(to:options:).md)
  Creates a JSON file with the contents of the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/dataframeprotocol-implementations)*