# init()

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates an empty table containing no rows or columns.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Discussion

Use this initializer to create an empty data table. Then, you add data columns with [`addColumn(_:named:)`](./addcolumn%28_,named%29-kkbw.md), untyped columns with [`addColumn(_:named:)`](./addcolumn%28_,named%29-9cb24.md), or another table with [`append(contentsOf:)`](./append%28contentsof%29.md).

## See Also

### Creating a data table
- [Creating a model from tabular data](../creating-a-model-from-tabular-data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws](./init%28contentsof,options%29.md)
  Creates a data table from an imported JSON or CSV file.
- [init(dictionary: [String : any MLDataValueConvertible]) throws](./init%28dictionary%29.md)
  Creates a data table from a dictionary of column names and data values.
- [init(namedColumns: [String : MLUntypedColumn]) throws](./init%28namedcolumns%29.md)
  Creates a data table from a dictionary of column names and untyped columns.
- [MLDataTable.ParsingOptions](./parsingoptions.md)
  The options for parsing a comma-separated values (CSV) file into a data table for a machine learning model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/init())*