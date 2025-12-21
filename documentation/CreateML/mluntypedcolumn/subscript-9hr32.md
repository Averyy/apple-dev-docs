# subscript(_:)

**Framework**: Create ML  
**Kind**: subscript

Creates a subset of the column by masking its elements with another untyped column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(mask: MLUntypedColumn) -> MLUntypedColumn { get }
```

#### Return Value

A new column.

#### Overview

Use this untyped column–based subscript to create a new column by masking a subset of the elements. The derived column will not include elements where `mask` contains a default value for its underlying type, such as:

- `0` in untyped `Int` columns
- `0.0` in untyped `Double` columns
- An empty string in untyped `String` columns

The derived column includes elements where the masking column has any other (nondefault) value.

See [`subscript(_:)`](mldatatable/subscript(_:)-10r4l.md) from [`MLDataTable`](mldatatable.md) for an example.

## Parameters

- `mask`: An untyped column indicating whether elements should be removed   (a default value) or included (any nondefault value) in the derived   column.

## See Also

- [subscript(_:)](mluntypedcolumn/subscript(_:).md)
  Accesses the element at the given position.
- [subscript(MLDataColumn<Bool>) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-8ot43.md)
  Creates a subset of the column by masking its elements with a data column of Booleans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/subscript(_:)-9hr32)*