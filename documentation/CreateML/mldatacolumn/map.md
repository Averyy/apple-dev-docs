# map(_:)

**Framework**: Create ML  
**Kind**: method

Creates a new column by applying the given thread-safe transform to every non-missing element of this column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func map<T>(_ lazyTransform: @escaping (Element) -> T) -> MLDataColumn<T> where T : MLDataValueConvertible
```

#### Return Value

A new column typed to the return type of `lazyTransform`.

## Parameters

- `lazyTransform`: A thread-safe element transformation function. The implementation of the transform you   provide should accept an   of the column and return a transformed value of a type that conforms to   .

## See Also

- [func mapMissing<T>((Element?) -> T?) -> MLDataColumn<T>](mldatacolumn/mapmissing(_:).md)
  Creates a new column, potentially with missing elements, by applying the given thread-safe transform to every element of the column, including missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/map(_:))*