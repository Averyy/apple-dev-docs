# map(_:)

**Framework**: Create ML  
**Kind**: method

Creates a new column, potentially with missing values, by applying a given thread-safe transform to every row in the data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func map<T>(_ lazyTransform: @escaping (MLDataTable.Row) -> T?) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new [`MLDataColumn`](mldatacolumn.md).

#### Discussion

This mapping function is the same as [`map(_:)`](mldatatable/map(_:)-92wrj.md) with the exception that this version’s `lazyTransform` parameter returns an optional (`T?`). Use this version of `map()` to create empty values by returning `nil` from your `lazyTransform`.

## Parameters

- `lazyTransform`: The implementation of your transform must accept a row from the data table and return   an optional type that conforms to  . If the   transform returns   for a given row, the corresponding element in   the new column will have a missing value.

## See Also

- [func map<T>((MLDataTable.Row) -> T) -> MLDataColumn<T>](mldatatable/map(_:)-92wrj.md)
  Creates a new column by applying a given thread-safe transform to every row in the data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/map(_:)-3yamp)*