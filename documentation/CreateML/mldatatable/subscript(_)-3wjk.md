# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

Retrieves or adds an untyped column with the specified name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(columnName: String) -> MLUntypedColumn { get set }
```

**Other overloads**:

```swift
subscript(mask: MLDataColumn<Bool>) -> MLDataTable { get }
```

```swift
subscript(mask: MLUntypedColumn) -> MLDataTable { get }
```

```swift
subscript(slice: Range<Int>) -> MLDataTable { get }
```

```swift
subscript<Element>(columnName: String) -> MLDataColumn<Element> where Element : MLDataValueConvertible { get set }
```

```swift
subscript<R>(slice: R) -> MLDataTable where R : RangeExpression, R.Bound == Int { get }
```

```swift
subscript<S>(columnNames: S) -> MLDataTable where S : Sequence, S.Element == String { get }
```

## Return Value

A new [`MLUntypedColumn`](../mluntypedcolumn.md) with the specified name, if it exists; otherwise an invalid column.

## Overview

Use this subscript to retrieve an [`MLUntypedColumn`](../mluntypedcolumn.md) or add a new one to the data table.

> ❗ **Important**: The number of elements in the column must equal the number of rows in the data table. Otherwise, the data table will be invalidated.

![A table on the left with two columns plus a third semi-opaque column.](https://developer.apple.com/tutorials/images/com.apple.createml/MLDataTable-subscript(_:)-3wjk-1@2x.png)

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
let distanceInAU = table["Distance (AU)"]
```

> **Note**: Without a type annotation, the compiler uses this version of `subscript(_:)` instead of the equivalent [`subscript(_:)`](./subscript%28_%29-5tl9r.md) from [`MLDataColumn`](../mldatacolumn.md).

Use the untyped column’s multiplication operator to create a new column of data.

```swift
// Create a new column of Doubles by multiplying all the the values in
// `distanceInAU` by 149,597,870.7 (the number of km in an astronomical unit)
let distanceInKm = (distanceInAU * 149_597_870.700)
```

Finally, use the `subscript(_:)` to add the new column to a table with a different name.

```swift
table["Distance (km)"] = distanceInKm
```

> ❗ **Important**: To replace a column, use [`removeColumn(named:)`](./removecolumn%28named%29.md) before adding its replacement. Adding a column with the same name as one already in the data table may invalidate the data table.

## Parameters

- `columnName`: The name of the column to extract from or add to the datatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:)-3wjk)*