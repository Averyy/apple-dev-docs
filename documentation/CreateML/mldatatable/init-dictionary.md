# init(dictionary:)

**Framework**: Create ML  
**Kind**: init

Creates a data table from a dictionary of column names and data values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(dictionary: [String : any MLDataValueConvertible]) throws
```

#### Discussion

Use this initializer to create a data table from an in-memory [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary).

![A table of information about a book. Columns named “Title”, “Author”,](https://docs-assets.developer.apple.com/published/3426640fe0e03c0d418fc851e1dd6812/MLDataTable-init%28dictionary%3A%29-1%402x.png)

For example, to create a data table as shown above, first create a dictionary.

```swift
let data: [String: MLDataValueConvertible] = [
    "Title": ["Alice in Wonderland", "Hamlet", "Treasure Island", "Peter Pan"],
    "Author": ["Lewis Carroll", "William Shakespeare", "Robert L. Stevenson", "J. M. Barrie"],
    "Pages": [124, 98, 280, 94],
    "Genre": ["Fantasy", "Drama", "Adventure", "Fantasy"]
]
```

Then, use [`init(dictionary:)`](mldatatable/init(dictionary:).md) to create a data table from the dictionary.

```swift
let bookTable = try MLDataTable(dictionary: data)
```

The keys of the dictionary become the column names, and the value of each key becomes the element(s) of the corresponding column in the data table.

## Parameters

- `dictionary`: The dictionary of each column name and its associated data values.

## See Also

- [Creating a model from tabular data](creating-a-model-from-tabular-data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [init(contentsOf: URL, options: MLDataTable.ParsingOptions) throws](mldatatable/init(contentsof:options:).md)
  Creates a data table from an imported JSON or CSV file.
- [init(namedColumns: [String : MLUntypedColumn]) throws](mldatatable/init(namedcolumns:).md)
  Creates a data table from a dictionary of column names and untyped columns.
- [init()](mldatatable/init.md)
  Creates an empty table containing no rows or columns.
- [MLDataTable.ParsingOptions](mldatatable/parsingoptions.md)
  The options for parsing a comma-separated values (CSV) file into a data table for a machine learning model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/init(dictionary:))*