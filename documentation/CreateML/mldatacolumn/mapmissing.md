# mapMissing(_:)

**Framework**: Create ML  
**Kind**: method

Creates a new column, potentially with missing elements, by applying the given thread-safe transform to every element of the column, including missing elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func mapMissing<T>(_ lazyTransform: @escaping (Element?) -> T?) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new column.

## Parameters

- `lazyTransform`: A thread-safe element transformation function. The implementation of the transform you   provide should accept an   of the column and return a transformed value of a type that conforms to   . If the transform returns   for a given element, the corresponding element   in the new column will have a missing value.

## See Also

- [func map<T>((Element) -> T) -> MLDataColumn<T>](mldatacolumn/map(_:)-7kto3.md)
  Creates a new column by applying the given thread-safe transform to every non-missing element of this column.
- [func map<T>((Element) -> T?) -> MLDataColumn<T>](mldatacolumn/map(_:)-72ypl.md)
  Creates a new column, potentially with missing values, by applying the given thread-safe transform to every non-missing element of this column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/mapmissing(_:))*