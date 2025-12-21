# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the table by masking the rows with the given column of Booleans.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLDataColumn<Bool>) -> MLDataTable { get }
```

#### Return Value

A new data table.

#### Overview

Use this Boolean column–based subscript to create a new table by masking a subset of the table rows.

![A table of book titles and genres such as “Hamlet” and “Drama” on the](https://docs-assets.developer.apple.com/published/77efab88ddfc6edd3497ca0c3cd9ab26/MLDataTable-subscript%28_%3A%29-3opgl-1%402x.png)

For example, to filter the values in a data table as shown above, begin by creating a table with the original data.

```swift
let data: [String: MLDataValueConvertible] = [
    "Title": ["Alice in Wonderland", "Hamlet", "Treasure Island", "Peter Pan"],
    "Genre": ["Fantasy", "Drama", "Adventure", "Fantasy"]
]

let table = try? MLDataTable(dictionary: data) else {
    fatalError("Invalid dictionary data")
}
```

After you create the table, use column arithmetic operators or the [`map(_:)`](mldatatable/map(_:)-92wrj.md) method to build a row mask. The subscript uses the Boolean values in the row mask to determine whether to keep a row.

```swift
// Retrieve the "Genre" column from the table.
guard let genreColumn = table["Genre", String.self] else {
    fatalError("Missing or invalid 'genre' column in table.")
}

// Create a new column of Booleans by comparing all of the values
// in `Genre` with `Fantasy` using the
// `!=(MLDataColumn<String>, String) -> MLDataColumn<Bool>` operator.
let noFantasyMask = genreColumn != "Fantasy"
```

Use `subscript(mask: MLDataColumn<Bool>)` with the Boolean column–row mask to create a filtered table.

```swift
let noFantasyTable = table[noFantasyMask]
```

## Parameters

- `mask`: A Boolean column indicating whether rows should be kept ( )   or removed ( ) in the derived table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-3opgl)*