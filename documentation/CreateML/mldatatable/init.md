# init()

**Framework**: Create ML  
**Kind**: init

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

Use this initializer to create an empty data table. Then, you add data columns with [`addColumn(_:named:)`](mldatatable/addcolumn(_:named:)-kkbw.md), untyped columns with [`addColumn(_:named:)`](mldatatable/addcolumn(_:named:)-9cb24.md), or another table with [`append(contentsOf:)`](mldatatable/append(contentsof:).md).

## See Also

- [Creating a Model from Tabular Data](creating_a_model_from_tabular_data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws](mldatatable/init(contentsof:options:).md)
  Creates a data table from an imported JSON or CSV file.
- [init(dictionary: [String : any MLDataValueConvertible]) throws](mldatatable/init(dictionary:).md)
  Creates a data table from a dictionary of column names and data values.
- [init(namedColumns: [String : MLUntypedColumn]) throws](mldatatable/init(namedcolumns:).md)
  Creates a data table from a dictionary of column names and untyped columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/init())*