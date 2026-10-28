# DataFrame.Slice

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

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

## Overview

A slice is an arbitrary set of rows from a data frame. For example, a slice might contain rows 0–3, 5–9, and 101 from its underlying data frame.

## Topics

### Inspecting a Slice
- [var shape: (rows: Int, columns: Int)](./slice/shape.md)
  The number of rows and columns in the slice.
- [var columns: [AnyColumnSlice]](./slice/columns.md)
  The entire slice as a collection of columns.
- [var rows: DataFrame.Rows](./slice/rows.md)
  The entire slice as a collection of rows.
- [var base: DataFrame](./slice/base.md)
  The underlying data frame.
### Creating a Slice by Selecting a Column
- [subscript<T>(ColumnID<T>) -> DiscontiguousColumnSlice<T>](./slice/subscript%28_%29-32h9z.md)
  Returns a column you select by its column identifier.
- [subscript<T>(column _: Int, T.Type) -> DiscontiguousColumnSlice<T>](./slice/subscript%28column,_%29.md)
  Returns a column you select by its index.
- [subscript<T>(String, T.Type) -> DiscontiguousColumnSlice<T>](./slice/subscript%28_,_%29.md)
  Returns a column you select by its name and type.
- [subscript(String) -> AnyColumnSlice](./slice/subscript%28_%29-18kdy.md)
  Returns a column you select by its name.
- [subscript(dynamicMember _: String) -> AnyColumnSlice](./slice/subscript%28dynamicmember%29.md)
  Returns a column you select by its name to support dynamic-member lookup.
### Creating a Slice by Selecting Multiple Columns
- [subscript<S>(S) -> DataFrame.Slice](./slice/subscript%28_%29-5y42o.md)
  Generates a data frame slice that includes the columns in a sequence of column names.
- [func selecting<S>(columnNames: S) -> DataFrame.Slice](./slice/selecting%28columnnames%29-9l8oe.md)
  Generates a data frame slice that includes the columns you select with a sequence of names.
- [func selecting(columnNames: String...) -> DataFrame.Slice](./slice/selecting%28columnnames%29-48kji.md)
  Generates a data frame slice that includes the columns you select with a list of names.
### Creating a Slice by Selecting Rows
- [func prefix(Int) -> DataFrame.Slice](./slice/prefix%28_%29.md)
  Returns a new slice that contains the initial elements of the original slice.
- [func prefix(upTo: Int) -> DataFrame.Slice](./slice/prefix%28upto%29.md)
  Returns a new slice that contains the initial elements of the original slice up to, but not including, the element at a position.
- [func prefix(through: Int) -> DataFrame.Slice](./slice/prefix%28through%29.md)
  Returns a new slice that contains the initial elements of the original slice up to and including the element at a position.
- [func suffix(Int) -> DataFrame.Slice](./slice/suffix%28_%29.md)
  Returns a new slice that contains the final elements of the original slice.
- [func suffix(from: Int) -> DataFrame.Slice](./slice/suffix%28from%29.md)
  Returns a new slice that contains the final elements of the original slice beginning with the element at a position.
### Creating a Slice by Filtering Rows
- [func filter<T>(on: ColumnID<T>, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./slice/filter%28on,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.
- [func filter<T>(on: String, T.Type, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./slice/filter%28on,_,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by name.
### Grouping Rows
- [struct RowGrouping](../rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](./slice/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [protocol RowGroupingProtocol](../rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.
### Summarizing a Slice
- [func summary() -> DataFrame](./slice/summary%28%29.md)
  Generates a data frame that summarizes the columns of the data frame slice.
- [func summary(of: String...) -> DataFrame](./slice/summary%28of%29.md)
  Generates a data frame that summarizes the columns you select by name.
- [func summary(ofColumns: Int...) -> DataFrame](./slice/summary%28ofcolumns%29.md)
  Generates a data frame that summarizes the columns you select by index.
- [enum SummaryColumnIDs](../summarycolumnids.md)
  The summary data frame column identifiers.
### Comparing Slices
- [static func == (DataFrame.Slice, DataFrame.Slice) -> Bool](./slice/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the slices are equal.
### Describing a Slice
- [var description: String](./slice/description.md)
  A text representation of the data frame slice.
- [var debugDescription: String](./slice/debugdescription.md)
  A text representation of the data frame slice suitable for debugging.
- [var customMirror: Mirror](./slice/custommirror.md)
  A mirror that reflects the data frame slice.
### Hashing a Slice
- [func hash(into: inout Hasher)](./slice/hash%28into%29.md)
  Hashes the essential components of the data frame slice by feeding them into a hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./slice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./slice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./slice/customstringconvertible-implementations.md)
- [Equatable Implementations](./slice/equatable-implementations.md)
- [Hashable Implementations](./slice/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [DataFrameProtocol](../dataframeprotocol.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Creating a Data Frame from Other Data Frames
- [init(DataFrame.Slice)](./init%28_%29.md)
  Creates a new data frame with a slice of rows from another data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice)*