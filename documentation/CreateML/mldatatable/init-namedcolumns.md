# init(namedColumns:)

**Framework**: Create ML  
**Kind**: init

Creates a data table from a dictionary of column names and untyped columns.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(namedColumns: [String : MLUntypedColumn]) throws
```

#### Discussion

Use this initializer to create a data table from untyped columns.

![A table of information about a book. Columns named “Title”, “Author”,](https://docs-assets.developer.apple.com/published/3426640fe0e03c0d418fc851e1dd6812/MLDataTable-init%28namedColumns%3A%29-1%402x.png)

For example, to create a data table as shown above, first create your untyped columns.

```swift
let pages = MLUntypedColumn([124, 98, 280, 94])
let genre = MLUntypedColumn(["Fantasy", "Drama", "Adventure", "Fantasy"])
let title = MLUntypedColumn(["Alice in Wonderland", "Hamlet", "Treasure Island", "Peter Pan"])
let author = MLUntypedColumn(["Lewis Carroll", "William Shakespeare", "Robert L. Stevenson", "J. M. Barrie"])
```

Then, use [`init(namedColumns:)`](mldatatable/init(namedcolumns:).md) to create a data table from the columns paired with their names.

```swift
let bookTable = try MLDataTable(namedColumns: ["Title": title,
                                               "Author": author,
                                               "Pages": pages,
                                               "Genre": genre])
```

## Parameters

- `namedColumns`: The dictionary of each column name and its associated untyped column data.

## See Also

- [Creating a Model from Tabular Data](creating_a_model_from_tabular_data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws](mldatatable/init(contentsof:options:).md)
  Creates a data table from an imported JSON or CSV file.
- [init(dictionary: [String : any MLDataValueConvertible]) throws](mldatatable/init(dictionary:).md)
  Creates a data table from a dictionary of column names and data values.
- [init()](mldatatable/init.md)
  Creates an empty table containing no rows or columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/init(namedcolumns:))*