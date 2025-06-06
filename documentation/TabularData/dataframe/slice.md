# DataFrame.Slice

**Framework**: TabularData  
**Kind**: struct

A set of a data frame’s rows you create by using a method from a data frame instance or another data frame slice.

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
@dynamicMemberLookup
struct Slice
```

#### Overview

A slice is an arbitrary set of rows from a data frame. For example, a slice might contain rows 0–3, 5–9, and 101 from its underlying data frame.

## Topics

### Inspecting a Slice
- [var isEmpty: Bool](dataframe/slice/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframe/slice/shape.md)
  The number of rows and columns in the slice.
- [var columns: [AnyColumnSlice]](dataframe/slice/columns.md)
  The entire slice as a collection of columns.
- [var rows: DataFrame.Rows](dataframe/slice/rows.md)
  The entire slice as a collection of rows.
- [var base: DataFrame](dataframe/slice/base.md)
  The underlying data frame.
### Creating a Slice by Selecting a Column
- [subscript<T>(ColumnID<T>) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(_:)-32h9z.md)
  Returns a column you select by its column identifier.
- [subscript<T>(column _: Int, T.Type) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(column:_:).md)
  Returns a column you select by its index.
- [subscript<T>(String, T.Type) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(_:_:).md)
  Returns a column you select by its name and type.
- [subscript(String) -> AnyColumnSlice](dataframe/slice/subscript(_:)-18kdy.md)
  Returns a column you select by its name.
- [subscript(dynamicMember _: String) -> AnyColumnSlice](dataframe/slice/subscript(dynamicmember:).md)
  Returns a column you select by its name to support dynamic-member lookup.
### Creating a Slice by Selecting Multiple Columns
- [subscript<S>(S) -> DataFrame.Slice](dataframe/slice/subscript(_:)-5y42o.md)
  Generates a data frame slice that includes the columns in a sequence of column names.
- [func selecting<S>(columnNames: S) -> DataFrame.Slice](dataframe/slice/selecting(columnnames:)-9l8oe.md)
  Generates a data frame slice that includes the columns you select with a sequence of names.
- [func selecting(columnNames: String...) -> DataFrame.Slice](dataframe/slice/selecting(columnnames:)-48kji.md)
  Generates a data frame slice that includes the columns you select with a list of names.
### Creating a Slice by Selecting Rows
- [func prefix(Int) -> DataFrame.Slice](dataframe/slice/prefix(_:).md)
  Returns a new slice that contains the initial elements of the original slice.
- [func prefix(upTo: Int) -> DataFrame.Slice](dataframe/slice/prefix(upto:).md)
  Returns a new slice that contains the initial elements of the original slice up to, but not including, the element at a position.
- [func prefix(through: Int) -> DataFrame.Slice](dataframe/slice/prefix(through:).md)
  Returns a new slice that contains the initial elements of the original slice up to and including the element at a position.
- [func suffix(Int) -> DataFrame.Slice](dataframe/slice/suffix(_:).md)
  Returns a new slice that contains the final elements of the original slice.
- [func suffix(from: Int) -> DataFrame.Slice](dataframe/slice/suffix(from:).md)
  Returns a new slice that contains the final elements of the original slice beginning with the element at a position.
### Creating a Slice by Filtering Rows
- [func filter<T>(on: ColumnID<T>, (T?) throws -> Bool) rethrows -> DataFrame.Slice](dataframe/slice/filter(on:_:).md)
  Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.
- [func filter<T>(on: String, T.Type, (T?) throws -> Bool) rethrows -> DataFrame.Slice](dataframe/slice/filter(on:_:_:).md)
  Returns a selection of rows that satisfy a predicate in the columns you select by name.
### Creating Two Slices by Splitting Rows
- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/slice/randomsplit(by:seed:).md)
  Generates two data frame slices by randomly splitting the rows of the data table.
- [func randomSplit<G>(by: Double, using: inout G) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/slice/randomsplit(by:using:).md)
  Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.
### Creating Two Data Frames by Splitting Rows
- [func stratifiedSplit(on: String, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.
- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.
- [func stratifiedSplit<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.
### Creating a Data Frame by Sorting a Column
- [func sorted(on: String, order: Order) -> DataFrame](dataframe/slice/sorted(on:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.
- [func sorted<T>(on: String, T.Type, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:order:)-37i2f.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type.
- [func sorted<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/slice/sorted(on:_:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name and type, with a predicate.
- [func sorted<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows -> DataFrame](dataframe/slice/sorted(on:by:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier, with a predicate.
### Creating a Data Frame by Sorting Multiple Columns
- [func sorted<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:order:)-xr0h.md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to two columns that you select by their column identifiers.
- [func sorted<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order) -> DataFrame](dataframe/slice/sorted(on:_:_:order:).md)
  Generates a data frame by copying the data frame’s rows and then sorting the rows according to three columns that you select by their column identifiers.
### Creating a Data Frame by Joining with Another Data Frame
- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-2glok.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1misl.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-3zgye.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframe/slice/joined(_:on:kind:)-1lz6j.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.
### Grouping Rows
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-13w3o.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](dataframe/slice/grouped(by:timeunit:)-696t5.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/slice/grouped(by:transform:)-5eoog.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](dataframe/slice/grouped(by:transform:)-7e9bm.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [struct RowGrouping](rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](dataframe/slice/grouped(by:).md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:).md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](dataframe/slice/grouped(by:_:_:).md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.
### Summarizing a Slice
- [func summary() -> DataFrame](dataframe/slice/summary.md)
  Generates a data frame that summarizes the columns of the data frame slice.
- [func summary(of: String...) -> DataFrame](dataframe/slice/summary(of:).md)
  Generates a data frame that summarizes the columns you select by name.
- [func summary(ofColumns: Int...) -> DataFrame](dataframe/slice/summary(ofcolumns:).md)
  Generates a data frame that summarizes the columns you select by index.
- [enum SummaryColumnIDs](summarycolumnids.md)
  The summary data frame column identifiers.
### Saving a Slice to a CSV
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframe/slice/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/slice/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.
### Comparing Slices
- [static func == (DataFrame.Slice, DataFrame.Slice) -> Bool](dataframe/slice/==(_:_:).md)
  Returns a Boolean that indicates whether the slices are equal.
- [static func != (Self, Self) -> Bool](dataframe/slice/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Describing a Slice
- [var description: String](dataframe/slice/description.md)
  A text representation of the data frame slice.
- [var debugDescription: String](dataframe/slice/debugdescription.md)
  A text representation of the data frame slice suitable for debugging.
- [func description(options: FormattingOptions) -> String](dataframe/slice/description(options:).md)
  Generates a text representation of the data frame type.
- [var customMirror: Mirror](dataframe/slice/custommirror.md)
  A mirror that reflects the data frame slice.
### Hashing a Slice
- [func hash(into: inout Hasher)](dataframe/slice/hash(into:).md)
  Hashes the essential components of the data frame slice by feeding them into a hasher.
### Type Aliases
- [DataFrame.Slice.ColumnType](dataframe/slice/columntype.md)
  A type that conforms to the type-erased column protocol.
### Default Implementations
- [CustomDebugStringConvertible Implementations](dataframe/slice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](dataframe/slice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](dataframe/slice/customstringconvertible-implementations.md)
- [DataFrameProtocol Implementations](dataframe/slice/dataframeprotocol-implementations.md)
- [Equatable Implementations](dataframe/slice/equatable-implementations.md)
- [Hashable Implementations](dataframe/slice/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataFrameProtocol](dataframeprotocol.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(DataFrame.Slice)](dataframe/init(_:).md)
  Creates a new data frame with a slice of rows from another data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice)*