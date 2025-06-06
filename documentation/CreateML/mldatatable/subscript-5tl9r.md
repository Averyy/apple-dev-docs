# subscript(_:)

**Framework**: Createml  
**Kind**: subscript

Retrieves or adds a typed column with the specified name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<Element>(columnName: String) -> MLDataColumn<Element> where Element : MLDataValueConvertible { get set }
```

#### Return Value

A new [`MLDataColumn`](mldatacolumn.md) with the specified name and inferred type, if it exists; otherwise an invalid column.

#### Overview

Use this subscript to retrieve an [`MLDataColumn`](mldatacolumn.md) or add a new one to the data table.

> ❗ **Important**: The number of elements in the column must equal the number of rows in the data table. Otherwise, the data table will be invalidated.

![A table on the left with two columns plus a third semi-opaque column.](https://docs-assets.developer.apple.com/published/d47258a4254c249703f7c2ab6c960289/MLDataTable-subscript%28_%3A%29-5tl9r-1%402x.png)

For example, to extract, convert, and add a column as shown above, begin by creating a data table.

```swift
let data: [String: MLDataValueConvertible] = [
    "Planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Distance (AU)": [0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06]
]

var table = try MLDataTable(dictionary: data)
```

After creating the table, extract a column.

```swift
let distanceInAU: MLDataColumn<Double> = table["Distance (AU)"]
```

> **Note**: By explicitly adding the type annotation `MLDataColumn<Double>`, the compiler uses this version of `subscript(_:)` instead of the equivalent [`subscript(_:)`](mldatatable/subscript(_:)-3wjk.md) from [`MLUntypedColumn`](mluntypedcolumn.md).

Use the column’s multiplication operator to create a new column of data.

```swift
// Create a new column of Doubles by multiplying all the the values in
// `distanceInAU` by 149,597,870.7 (the number of km in an astronomical unit)
let distanceInKm = (distanceInAU * 149_597_870.700)
```

Finally, use the `subscript(_:)` to add the new column to the table with a different name.

```swift
table["Distance (km)"] = distanceInKm
```

> ❗ **Important**: To replace a column, use [`removeColumn(named:)`](mldatatable/removecolumn(named:).md) before adding its replacement. Adding a column with the same name as one already in the data table may invalidate the data table.

## Parameters

- `columnName`: The name of the column to extract from or add to the data table.

## See Also

- [subscript<T>(String, T.Type) -> MLDataColumn<T>?](mldatatable/subscript(_:_:).md)
  Retrieves a column with the specified name and type.
- [subscript(String) -> MLUntypedColumn](mldatatable/subscript(_:)-3wjk.md)
  Retrieves or adds an untyped column with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-5tl9r)*