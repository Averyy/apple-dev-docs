# map(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func map<T>(_ lazyTransform: @escaping (MLDataTable.Row) -> T) -> MLDataColumn<T> where T : MLDataValueConvertible
```

## Return Value

A new [`MLDataColumn`](../mldatacolumn.md).

## Discussion

This mapping function is the same as [`map(_:)`](./map%28_%29-92wrj.md) with the exception that this version’s `lazyTransform` parameter returns an optional (`T?`). Use this version of `map()` to create empty values by returning `nil` from your `lazyTransform`.

## Parameters

- `lazyTransform`: A thread-safe row transformation function.

  The implementation of your transform must accept a row from the data table and return an optional type that conforms to [`MLDataValueConvertible`](../mldatavalueconvertible.md). If the transform returns `nil` for a given row, the corresponding element in the new column will have a missing value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/map(_:)-3yamp)*