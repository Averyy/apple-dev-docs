# Row Operations

**Framework**: TabularData  
**Role**: API Collection

Add, select, and group rows within a data frame.

## Overview

Use these methods to interact with a data frame’s elements by row.

## Topics

### Adding a row
- [func appendEmptyRow()](./dataframe/appendemptyrow%28%29.md)
  Adds an empty row to the data frame.
- [func append(row: Any?...)](./dataframe/append%28row%29-3p6lx.md)
  Adds a comma-separated, or variadic, list of values as a row to the data frame.
- [func append(valuesByColumn: [String : Any?])](./dataframe/append%28valuesbycolumn%29.md)
  Adds a dictionary’s values as a row to the data frame.
### Adding a row from a data frame
- [func append(row: DataFrame.Row)](./dataframe/append%28row%29-6wvcq.md)
  Adds a row of values to the data frame.
- [func insert(row: DataFrame.Row, at: Int)](./dataframe/insert%28row,at%29.md)
  Adds a row of values at a position in the data frame.
### Adding multiple rows from a data frame
- [func append(DataFrame)](./dataframe/append%28_%29-36sor.md)
  Adds the rows of another data frame.
- [func append(rowsOf: DataFrame)](./dataframe/append%28rowsof%29.md)
  Adds the rows of another data frame that has the same column names and types.
- [func append(DataFrame.Slice)](./dataframe/append%28_%29-5l4c5.md)
  Adds the rows of a slice from a data frame.
### Accessing a row
- [subscript(row _: Int) -> DataFrame.Row](./dataframe/subscript%28row%29.md)
  Accesses a row by its index.
### Removing a row
- [func removeRow(at: Int)](./dataframe/removerow%28at%29.md)
  Removes a row from the data frame.
### Creating a slice by selecting rows
- [func prefix(Int) -> DataFrame.Slice](./dataframe/prefix%28_%29.md)
  Returns a slice that contains the initial rows up to a maximum length.
- [func suffix(Int) -> DataFrame.Slice](./dataframe/suffix%28_%29.md)
  Returns a slice that contains the final rows up to a maximum length.
- [subscript<C>(C) -> DataFrame.Slice](./dataframe/subscript%28_%29-6tuca.md)
  Returns a slice of the rows by masking its elements with a Boolean column.
- [subscript(Range<Int>) -> DataFrame.Slice](./dataframeprotocol/subscript%28_%29.md)
  Accesses a slice of the data frame type with an index range.
- [subscript<R>(R) -> DataFrame.Slice](./dataframeprotocol/subscript%28_%29-8hly3.md)
  Accesses rows of a data frame type with an index range expression.
### Creating a slice by filtering rows
- [func filter((DataFrame.Row) throws -> Bool) rethrows -> DataFrame.Slice](./dataframe/filter%28_%29.md)
  Returns a selection of rows that satisfy a predicate.
- [func filter<T>(on: String, T.Type, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./dataframe/filter%28on,_,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by name.
- [func filter<T>(on: ColumnID<T>, (T?) throws -> Bool) rethrows -> DataFrame.Slice](./dataframe/filter%28on,_%29.md)
  Returns a selection of rows that satisfy a predicate in the columns you select by column identifier.
### Creating two slices by splitting rows
- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](./dataframeprotocol/randomsplit%28by,seed%29.md)
  Generates two data frame slices by randomly splitting the rows of the data table.
- [func randomSplit<G>(by: Double, using: inout G) -> (DataFrame.Slice, DataFrame.Slice)](./dataframeprotocol/randomsplit%28by,using%29.md)
  Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.
### Grouping rows
- [func grouped(by: ColumnID<Date>, timeUnit: Calendar.Component) -> RowGrouping<Int>](./dataframeprotocol/grouped%28by,timeunit%29-78cy.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by column identifier.
- [func grouped(by: String, timeUnit: Calendar.Component) -> RowGrouping<Int>](./dataframeprotocol/grouped%28by,timeunit%29-7s782.md)
  Creates a grouping of rows that the method selects by choosing unique units of time in a date column you select by name.
- [func grouped<InputKey, GroupingKey>(by: ColumnID<InputKey>, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](./dataframeprotocol/grouped%28by,transform%29-3aade.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by column identifier.
- [func grouped<InputKey, GroupingKey>(by: String, transform: (InputKey?) -> GroupingKey?) -> RowGrouping<GroupingKey>](./dataframeprotocol/grouped%28by,transform%29-3cr4p.md)
  Creates a grouping of rows that the method selects by choosing unique values the transform closure creates with elements of a column you select by name.
- [struct RowGrouping](./rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [func grouped(by: String) -> any RowGroupingProtocol](./dataframe/grouped%28by%29.md)
  Creates a grouping of rows that the method selects by choosing unique values in a column.
- [func grouped<T0, T1>(by: ColumnID<T0>, ColumnID<T1>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_%29.md)
  Creates a grouping from two columns of different types.
- [func grouped<T0, T1, T2>(by: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>) -> some RowGroupingProtocol](./dataframeprotocol/grouped%28by,_,_%29.md)
  Creates a grouping from three columns of different types.
- [protocol RowGroupingProtocol](./rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.
### Supporting types
- [DataFrame.Row](./dataframe/row.md)
  A single row within a data frame.
- [DataFrame.Slice](./dataframe/slice.md)
  A set of a data frame’s rows you create by using a method from a data frame instance or another data frame slice.

## See Also

### Working with rows and columns
- [Column Operations](./dataframe-column-operations.md)
  Add, modify, and remove columns within a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe-row-operations)*