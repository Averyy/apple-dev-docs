# mapMissing(_:)

**Framework**: Create ML  
**Kind**: method

Creates a new column of typed values by applying the given thread-safe transform to every element of this untyped column, including missing elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func mapMissing<T>(_ lazyTransform: @escaping (MLDataValue) -> T?) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new `MLDataColumn` column.

## Parameters

- `lazyTransform`: A thread-safe element transformation function. The   implementation of the transform you provide should accept an element of   the column and return a transformed value of a type that conforms to   . If the transform returns   for a given   element, the corresponding element in the new column will have a missing   value.

## See Also

- [func map(_:)](mluntypedcolumn/map(_:).md)
  Creates a new column of typed values by applying the given thread-safe transform to every non-missing element of this untyped column.
- [func map<T>((MLDataValue) -> T) -> MLDataColumn<T>](mluntypedcolumn/map(_:)-139qy.md)
  Creates a new column of typed values by applying the given thread-safe transform to every non-missing element of this untyped column.
- [func map<T>((MLDataValue) -> T?) -> MLDataColumn<T>](mluntypedcolumn/map(_:)-9v61j.md)
  Creates a new column of typed values, potentially with missing values, by applying the given thread-safe transform to every non-missing element of this untyped column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/mapmissing(_:))*