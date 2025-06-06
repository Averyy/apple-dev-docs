# map(_:)

**Framework**: Create ML  
**Kind**: method

Creates a new column by applying a given thread-safe transform to every row in the data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func map<T>(_ lazyTransform: @escaping (MLDataTable.Row) -> T) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new [`MLDataColumn`](mldatacolumn.md).

#### Discussion

Use this method to create a new column derived from the existing data in the table. The closure you pass evaluates lazily only when the transformed values are needed for a subsequent operation. Your implementation should accept a data table row and must be thread-safe because the framework may invoke the closure concurrently on unspecified threads.

![A table on the left with “Day” and “Temperature” columns. The first](https://docs-assets.developer.apple.com/published/2978b2734af4be5b47c260d7953162ee/MLDataTable-map%28_%3A%29-92wrj-1%402x.png)

For example, to perform the column derivation operation shown above, begin by creating a table of data.

```swift
let data: [String: MLDataValueConvertible] = [
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [91.3, 85.8, 79.5, 83.4, 72.2]
]

var table = try MLDataTable(dictionary: data)
```

After creating the table, use [`map(_:)`](mldatatable/map(_:)-92wrj.md) to create a new column of data from the original data. The example closure implementation below is stateless and safe to invoke concurrently on any thread, so no synchronization is necessary.

```swift
let derivedColumn = table.map { row -> String in
    guard let day = row["Day"]?.stringValue,
          let temperature = row["Temperature"]?.doubleValue else {
            fatalError("Missing or invalid columns in row.")
    }
    return String(format: "%@ %.1fº", day, temperature)
}
```

Then use [`addColumn(_:named:)`](mldatatable/addcolumn(_:named:)-kkbw.md) to add the derived column to a table.

```swift
table.addColumn(derivedColumn, named: "Description")
```

## Parameters

- `lazyTransform`: The implementation of your transform must accept a row from the data table and return   a type that conforms to  .

## See Also

- [Preventing Timing Problems When Using Closures](../Swift/preventing-timing-problems-when-using-closures.md)
  Understand how different API calls to your closures can affect your app.
- [func map<T>((MLDataTable.Row) -> T?) -> MLDataColumn<T>](mldatatable/map(_:)-3yamp.md)
  Creates a new column, potentially with missing values, by applying a given thread-safe transform to every row in the data table.
- [func map<T>((MLDataTable.Row) -> T?) -> MLDataColumn<T>](mldatatable/map(_:)-3yamp.md)
  Creates a new column, potentially with missing values, by applying a given thread-safe transform to every row in the data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/map(_:)-92wrj)*