# MLDataTable

**Framework**: Create ML  
**Kind**: struct

A table of data for training or evaluating a machine learning model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLDataTable
```

## Mentions

- [Creating a word tagger model](creating-a-word-tagger-model.md)
- [Creating a text classifier model](creating-a-text-classifier-model.md)

#### Overview

[`MLDataTable`](mldatatable.md) is Create ML’s version of a spreadsheet in which each row represents an entity (such as a book, in the example below) with observable features. Each column ([`MLDataColumn`](mldatacolumn.md) or [`MLUntypedColumn`](mluntypedcolumn.md)) in the table represents an observable feature of that entity, such as a book’s title or author.

![A table of information about a book. Columns named “Title”, “Author”,](https://docs-assets.developer.apple.com/published/64120429043de5dfe14896956373df1d/MLDataTable-1%402x.png)

In most cases you interact with columns using the typed [`MLDataColumn`](mldatacolumn.md), especially when you need to directly access the contents of a column. You can also interact with columns using [`MLUntypedColumn`](mluntypedcolumn.md), if the underlying type of the column isn’t important.

After you create a data table, you can modify it with methods like [`append(contentsOf:)`](mldatatable/append(contentsof:).md), [`addColumn(_:named:)`](mldatatable/addcolumn(_:named:)-kkbw.md), and [`removeColumn(named:)`](mldatatable/removecolumn(named:).md). You can also filter or map the contents of the data table to derive new data tables or new columns by using various subscripts and methods like [`dropDuplicates()`](mldatatable/dropduplicates().md) or [`map(_:)`](mldatatable/map(_:)-92wrj.md).

> **Note**: For a demonstration that creates and uses data tables, see [`Creating a model from tabular data`](creating-a-model-from-tabular-data.md).

Finally, when your data table is ready, use it to train and evaluate a model from these groups:

- Regressors like [`MLRegressor`](mlregressor.md) and its supporting types
- Classifiers like [`MLClassifier`](mlclassifier.md) and its supporting types
- Natural language processing types like [`MLTextClassifier`](mltextclassifier.md) and [`MLWordTagger`](mlwordtagger.md)

> **Note**: It’s easier to train an [`MLTextClassifier`](mltextclassifier.md) from folders and files with [`init(trainingData:parameters:)`](mltextclassifier/init(trainingdata:parameters:)-8n8vs.md) if your data is ready to use, as-is. Otherwise, use a data table to prepare your data before training a text classifier.

## Topics

### Creating a data table
- [Creating a model from tabular data](creating-a-model-from-tabular-data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws](mldatatable/init(contentsof:options:).md)
  Creates a data table from an imported JSON or CSV file.
- [init(dictionary: [String : any MLDataValueConvertible]) throws](mldatatable/init(dictionary:).md)
  Creates a data table from a dictionary of column names and data values.
- [init(namedColumns: [String : MLUntypedColumn]) throws](mldatatable/init(namedcolumns:).md)
  Creates a data table from a dictionary of column names and untyped columns.
- [init()](mldatatable/init.md)
  Creates an empty table containing no rows or columns.
- [MLDataTable.ParsingOptions](mldatatable/parsingoptions.md)
  The options for parsing a comma-separated values (CSV) file into a data table for a machine learning model.
### Getting the size of a data table
- [var size: (rows: Int, columns: Int)](mldatatable/size.md)
  The number of rows and columns in the data table.
### Transforming rows to generate a data column
- [func map(_:)](mldatatable/map(_:).md)
  Creates a new column by applying a given thread-safe transform to every row in the data table.
### Adding columns
- [func addColumn(_:named:)](mldatatable/addcolumn(_:named:).md)
  Adds an untyped column to the table.
- [struct MLDataColumn](mldatacolumn.md)
  A column of typed values in a data table.
- [struct MLUntypedColumn](mluntypedcolumn.md)
  A column of untyped values in a data table.
### Accessing columns
- [subscript(_:)](mldatatable/subscript(_:).md)
  Retrieves or adds an untyped column with the specified name.
- [subscript<T>(String, T.Type) -> MLDataColumn<T>?](mldatatable/subscript(_:_:).md)
  Retrieves a column with the specified name and type.
### Renaming columns
- [func renameColumn(named: String, to: String)](mldatatable/renamecolumn(named:to:).md)
  Changes the name of an existing column.
### Removing columns
- [func removeColumn(named: String)](mldatatable/removecolumn(named:).md)
  Removes the column with the specified name.
### Appending to a data table
- [func append(contentsOf: MLDataTable)](mldatatable/append(contentsof:).md)
  Appends the contents of the given data table to the end of this data table.
### Generating new data tables
- [Data table derivation operations](data-table-derivation-operations.md)
  Create new data tables by manipulating an existing data table.
### Splitting a data table
- [func randomSplitBySequence(proportion: Double, by: String, on: String, seed: Int) -> (MLDataTable, remaining: MLDataTable)](mldatatable/randomsplitbysequence(proportion:by:on:seed:).md)
- [func stratifiedSplit<RNG>(proportions: [Double], on: String, generator: inout RNG) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:generator:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplit(proportions: [Double], on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplit(proportions:on:seed:).md)
  Randomly split a MLDataTable into a number partitions while stratifying on a user-define label column.
- [func stratifiedSplitBySequence<RNG>(proportions: [Double], by: String, on: String, generator: inout RNG) throws -> MLDataTable](mldatatable/stratifiedsplitbysequence(proportions:by:on:generator:).md)
  Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.
- [func stratifiedSplitBySequence(proportions: [Double], by: String, on: String, seed: Int) throws -> MLDataTable](mldatatable/stratifiedsplitbysequence(proportions:by:on:seed:).md)
  Randomly split a MLDataTable into partitions on a user-define label column, while keeping rows from the same sequence in the original order.
### Getting information about a data table’s rows
- [MLDataTable.Row](mldatatable/row.md)
  A row of untyped values in a data table.
- [var rows: MLDataTable.Rows](mldatatable/rows-swift.property.md)
  The rows of data in the table.
- [MLDataTable.Rows](mldatatable/rows-swift.struct.md)
  A collection of rows in a data table.
### Getting information about a data table’s columns
- [var columnNames: MLDataTable.ColumnNames](mldatatable/columnnames-swift.property.md)
  The names of the columns in the data table.
- [MLDataTable.ColumnNames](mldatatable/columnnames-swift.struct.md)
  A collection of the names of the columns in a data table.
- [var columnTypes: [String : MLDataValue.ValueType]](mldatatable/columntypes.md)
  The type of the data in each column.
### Saving a data table
- [func write(to: URL) throws](mldatatable/write(to:).md)
  Exports a binary file of the data table to the given directory URL.
- [func write(toDirectory: String) throws](mldatatable/write(todirectory:).md)
  Exports a binary file of the data table to the given directory path.
- [func writeCSV(to: URL) throws](mldatatable/writecsv(to:).md)
  Exports a CSV file of the data table to the given directory URL.
- [func writeCSV(toFile: String) throws](mldatatable/writecsv(tofile:).md)
  Exports a CSV file of the data table to the given directory path.
### Visualizing a data table
- [func show() -> any MLStreamingVisualizable](mldatatable/show.md)
  Generates a visualization for the data in the table.
### Describing a data table
- [var description: String](mldatatable/description.md)
  A text representation of the data table.
- [var playgroundDescription: Any](mldatatable/playgrounddescription.md)
  A description of the data table shown in a playground.
### Handling data table errors
- [var isValid: Bool](mldatatable/isvalid.md)
  A Boolean value that indicates whether the data table is valid.
- [var error: (any Error)?](mldatatable/error.md)
  The underlying error present when the data table is invalid.
### Default Implementations
- [CustomPlaygroundDisplayConvertible Implementations](mldatatable/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatatable/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [enum MLDataValue](mldatavalue.md)
  The value of a cell in a data table.
- [Data visualizations](data-visualizations.md)
  Render images of data tables and columns in a playground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable)*