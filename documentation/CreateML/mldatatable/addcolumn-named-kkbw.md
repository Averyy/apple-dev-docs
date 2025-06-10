# addColumn(_:named:)

**Framework**: Create ML  
**Kind**: method

Adds a data column to the table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
mutating func addColumn<Element>(_ newColumn: MLDataColumn<Element>, named: String) where Element : MLDataValueConvertible
```

#### Discussion

Use this method to add a data column to a data table.

> ❗ **Important**: The number of elements in the column must equal the number of rows in the data table. Otherwise, the data table will be invalidated.

As an example, start with a data table variable.

```swift
let data: [String: MLDataValueConvertible] = [
    "Title": ["Alice in Wonderland", "Hamlet", "Treasure Island", "Peter Pan"],
    "Author": ["Lewis Carroll", "William Shakespeare", "Robert L. Stevenson", "J. M. Barrie"],
    "Pages": [124, 98, 280, 94],
]

var bookTable = try MLDataTable(dictionary: data)
```

Then use [`addColumn(_:named:)`](mldatatable/addcolumn(_:named:)-kkbw.md) to add a column to the table.

```swift
let pagesColumn = MLDataColumn([124, 98, 280, 94])
bookTable.addColumn(pagesColumn, named: "Pages")
```

## Parameters

- `newColumn`: A column to add to the data table.
- `named`: The name of the new column.

## See Also

- [struct MLDataColumn](mldatacolumn.md)
  A column of typed values in a data table.
- [func addColumn(MLUntypedColumn, named: String)](mldatatable/addcolumn(_:named:)-9cb24.md)
  Adds an untyped column to the table.
- [struct MLUntypedColumn](mluntypedcolumn.md)
  A column of untyped values in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/addcolumn(_:named:)-kkbw)*