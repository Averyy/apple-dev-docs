# subscript(_:_:)

**Framework**: Create ML  
**Kind**: subscript

Retrieves a column with the specified name and type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<T>(columnName: String, columnType: T.Type) -> MLDataColumn<T>? where T : MLDataValueConvertible { get }
```

#### Return Value

A new [`MLDataColumn`](mldatacolumn.md) with the specified name and type, if it exists; otherwise `nil`.

#### Overview

Use this subscript to get a typed [`MLDataColumn`](mldatacolumn.md), which is easier to work with than a [`MLUntypedColumn`](mluntypedcolumn.md) returned from [`subscript(_:)`](mldatatable/subscript(_:)-3wjk.md).

## Parameters

- `columnName`: The name of the column to extract.
- `columnType`: The underlying type of the column’s content.

## See Also

- [subscript(_:)](mldatatable/subscript(_:).md)
  Retrieves or adds an untyped column with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/subscript(_:_:))*