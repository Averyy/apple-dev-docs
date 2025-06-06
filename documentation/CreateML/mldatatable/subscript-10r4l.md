# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the table by masking the rows with the given untyped column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLUntypedColumn) -> MLDataTable { get }
```

#### Return Value

A new data table.

#### Overview

Use this untyped column–based subscript to create a new table by masking a subset of the table rows. The derived table will not include rows where `mask` contains a default value for its underlying type, such as:

- `0` in untyped `Int` columns
- `0.0` in untyped `Double` columns
- An empty string in untyped `String` columns

The derived data table includes rows where the masking column has any other (nondefault) value.

![A table of book information on the left with columns named “Title”,](https://docs-assets.developer.apple.com/published/e6d1f548b7d61ae8d264f690e5513d2e/MLDataTable-subscript%28_%3A%29-10r4l-1%402x.png)

For example, to filter the values in a data table as shown above, begin by creating a table with the original data.

```swift
let data: [String: MLDataValueConvertible] = [
    "Title": ["Alice in Wonderland", "Hamlet", "Dracula", "Peter Pan", "The Great Gatsby"],
    "Genre": ["Fantasy", "Drama", "Adventure", "Fantasy", "Drama"],
    "Pages": [124, 98, 0, 94, 0]
]

guard let table = try? MLDataTable(dictionary: data) else {
    fatalError("Invalid dictionary data")
}
```

After you create the table, use the `String`-based [`subscript(_:)`](mldatatable/subscript(_:)-3wjk.md) to extract a column.

```swift
// Create a new untyped column "pagesColumn" copied from the table’s "Pages" column
let pagesColumn = table["Pages"]
```

Use `subscript(mask: MLUntypedColumn)` with an untyped column–row mask to create a filtered table. The subscript uses the untyped values to determine whether to keep a row.

In this example, the untyped column `pagesColumn` has an underlying type of `Int`. The subscript removes any row with a value of `0` (the default value for `Int`) and keeps all other rows.

```swift
// Filter the table using pagesColumn.
// Each row with a value of 0 is removed.
let validPageCountTable = table[pagesColumn]
```

## Parameters

- `mask`: An untyped column indicating whether rows should be removed (a   default value) or included (any nondefault value) in the derived table.

## See Also

- [subscript(MLDataColumn<Bool>) -> MLDataTable](mldatatable/subscript(_:)-3opgl.md)
  Creates a subset of the table by masking the rows with the given column of Booleans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-10r4l)*