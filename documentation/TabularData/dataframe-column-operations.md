# Column Operations

**Framework**: TabularData  
**Role**: API Collection

Add, modify, and remove columns within a data frame.

## Overview

Use these methods to interact with a data frame’s elements by column.

## Topics

### Renaming a column
- [func renameColumn(String, to: String)](./dataframe/renamecolumn%28_,to%29.md)
  Renames a column in the data frame.
### Aliasing a column name
- [func addAlias(String, forColumn: String)](./dataframe/addalias%28_,forcolumn%29.md)
  Adds an alternative name for a column.
- [func columnNames(forAlias: String) -> [String]](./dataframe/columnnames%28foralias%29.md)
  Returns the column names for an alias.
- [func removeAlias(String)](./dataframe/removealias%28_%29.md)
  Removes an alternative name for a column.
### Adding a column
- [func append(column: AnyColumn)](./dataframe/append%28column%29-45s2v.md)
  Adds a type-erased column to the end of the data frame.
- [func append<T>(column: Column<T>)](./dataframe/append%28column%29-aema.md)
  Adds a typed column to the end of the data frame.
- [func insert(column: AnyColumn, at: Int)](./dataframe/insert%28column,at%29-784jb.md)
  Adds a type-erased column at a position in the data frame.
- [func insert<T>(column: Column<T>, at: Int)](./dataframe/insert%28column,at%29-5g6i9.md)
  Adds a typed column at a position in the data frame.
### Retrieving a column index
- [func indexOfColumn(String) -> Int?](./dataframe/indexofcolumn%28_%29.md)
  Returns the index of a column.
### Accessing a column
- [subscript(String) -> AnyColumn](./dataframe/subscript%28_%29-738lb.md)
  Accesses a column by its name.
- [subscript<T>(String, T.Type) -> Column<T>](./dataframe/subscript%28_,_%29-5walz.md)
  Accesses a column by its name and type.
- [subscript<T>(ColumnID<T>) -> Column<T>](./dataframe/subscript%28_%29-6mv5i.md)
  Accesses a column by its column identifier.
- [subscript(column _: Int) -> AnyColumn](./dataframe/subscript%28column%29.md)
  Accesses a column by its index.
- [subscript<T>(column _: Int, T.Type) -> Column<T>](./dataframe/subscript%28column,_%29.md)
  Accesses a column by its index and type.
- [subscript(dynamicMember _: String) -> AnyColumn](./dataframe/subscript%28dynamicmember%29.md)
  Accesses a column by its name to support dynamic-member lookup.
### Accessing a column as an array
- [subscript<T>(String, T.Type) -> [T?]](./dataframe/subscript%28_,_%29-6oqm0.md)
  Accesses a column as an array by its name.
### Replacing a column
- [func replaceColumn(String, with: AnyColumn)](./dataframe/replacecolumn%28_,with%29-2b3u3.md)
  Replaces a column in the data frame, by name, with a type-erased column.
- [func replaceColumn<T>(String, with: Column<T>)](./dataframe/replacecolumn%28_,with%29-4yub5.md)
  Replaces a column in the data frame, by name, with a typed column.
- [func replaceColumn<T>(ColumnID<T>, with: AnyColumn)](./dataframe/replacecolumn%28_,with%29-9sn9i.md)
  Replaces a column in the data frame, by column identifier, with a type-erased column.
- [func replaceColumn<T, U>(ColumnID<T>, with: Column<U>)](./dataframe/replacecolumn%28_,with%29-oa9g.md)
  Replaces a column in the data frame, by column identifier, with a typed column.
### Removing a column
- [func removeColumn(String) -> AnyColumn](./dataframe/removecolumn%28_%29-5zu7l.md)
  Removes a column you select by its name from the data frame.
- [func removeColumn<T>(ColumnID<T>) -> Column<T>](./dataframe/removecolumn%28_%29-qtea.md)
  Removes a column you select by its column identifier from the data frame.
### Transforming a column
- [func transformColumn<From, To>(ColumnID<From>, (From) throws -> To?) rethrows](./dataframe/transformcolumn%28_,_%29-2avtt.md)
  Applies a transform closure that modifies the nonempty elements of a column you select by column identifier.
- [func transformColumn<From, To>(ColumnID<From>, (From?) throws -> To?) rethrows](./dataframe/transformcolumn%28_,_%29-5s9en.md)
  Applies a transform closure that modifies the elements of a column you select by column identifier.
- [func transformColumn<From, To>(String, (From?) throws -> To?) rethrows](./dataframe/transformcolumn%28_,_%29-3czz0.md)
  Applies a transform closure that modifies the elements of a column you select by name.
- [func transformColumn<From, To>(String, (From) throws -> To?) rethrows](./dataframe/transformcolumn%28_,_%29-6cxpn.md)
  Applies a transform closure that modifies the nonempty elements of a column you select by name.
### Merging columns
- [func combineColumns<E1, E2, R>(String, String, into: String, transform: (E1?, E2?) throws -> R?) rethrows](./dataframe/combinecolumns%28_,_,into,transform%29-48ypf.md)
  Merges two columns that you select by name into a new column.
- [func combineColumns<E1, E2, R>(ColumnID<E1>, ColumnID<E2>, into: String, transform: (E1?, E2?) throws -> R?) rethrows](./dataframe/combinecolumns%28_,_,into,transform%29-85gix.md)
  Merges two columns that you select by column identifier into a new column.
- [func combineColumns<E1, E2, E3, R>(String, String, String, into: String, transform: (E1?, E2?, E3?) throws -> R?) rethrows](./dataframe/combinecolumns%28_,_,_,into,transform%29-4vyjn.md)
  Merges three columns that you select by name into a new column.
- [func combineColumns<E1, E2, E3, R>(ColumnID<E1>, ColumnID<E2>, ColumnID<E3>, into: String, transform: (E1?, E2?, E3?) throws -> R?) rethrows](./dataframe/combinecolumns%28_,_,_,into,transform%29-48g26.md)
  Merges three columns that you select by column identifier into a new column.
### Expanding a column
- [func explodeColumn<T>(String, T.Type)](./dataframe/explodecolumn%28_,_%29.md)
  Replaces each row in a collection column that you select by name, with a new row for each element in the original row’s collection.
- [func explodeColumn<T>(ColumnID<T>)](./dataframe/explodecolumn%28_%29.md)
  Replaces each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.
- [func explodingColumn<T>(String, T.Type) -> DataFrame](./dataframe/explodingcolumn%28_,_%29.md)
  Generates a data frame by replacing each row in a collection column that you select by name, with a new row for each element in the original row’s collection.
- [func explodingColumn<T>(ColumnID<T>) -> DataFrame](./dataframe/explodingcolumn%28_%29.md)
  Generates a data frame by replacing each row in a collection column that you select by column identifier, with a new row for each element in the original row’s collection.
### Encoding a column
- [func encodeColumn<T, Encoder>(String, T.Type, using: Encoder) throws](./dataframe/encodecolumn%28_,_,using%29.md)
  Encodes the elements of a column you select by name.
- [func encodeColumn<T, Encoder>(ColumnID<T>, using: Encoder) throws](./dataframe/encodecolumn%28_,using%29.md)
  Encodes the elements of a column you select by column identifier.
### Decoding a column
- [func decode<T, Decoder>(T.Type, inColumn: String, using: Decoder) throws](./dataframe/decode%28_,incolumn,using%29-443a9.md)
  Decodes the elements of a column you select by name.
- [func decode<T, Decoder>(T.Type, inColumn: ColumnID<Decoder.Input>, using: Decoder) throws](./dataframe/decode%28_,incolumn,using%29-2brfw.md)
  Decodes the elements of a column you select by column identifier.

## See Also

### Working with rows and columns
- [Row Operations](./dataframe-row-operations.md)
  Add, select, and group rows within a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe-column-operations)*