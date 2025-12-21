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
### Grouping Rows
- [struct RowGrouping](rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](dataframe/slice/grouped(by:).md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
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
### Comparing Slices
- [static func == (DataFrame.Slice, DataFrame.Slice) -> Bool](dataframe/slice/==(_:_:).md)
  Returns a Boolean that indicates whether the slices are equal.
### Describing a Slice
- [var description: String](dataframe/slice/description.md)
  A text representation of the data frame slice.
- [var debugDescription: String](dataframe/slice/debugdescription.md)
  A text representation of the data frame slice suitable for debugging.
- [var customMirror: Mirror](dataframe/slice/custommirror.md)
  A mirror that reflects the data frame slice.
### Hashing a Slice
- [func hash(into: inout Hasher)](dataframe/slice/hash(into:).md)
  Hashes the essential components of the data frame slice by feeding them into a hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](dataframe/slice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](dataframe/slice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](dataframe/slice/customstringconvertible-implementations.md)
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