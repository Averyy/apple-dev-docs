# suffix(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Creates a subset of the column, given a number of final elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func suffix(_ maxLength: Int = 10) -> MLDataColumn<Element>
```

Available when `Element` conforms to `MLDataValueConvertible`.

## Return Value

A new column.

## Parameters

- `maxLength`: An integer that limits the number of elements to use from the end of the column. The default value is `10`.

## See Also

### Selecting elements to generate a column
- [subscript(Range<Int>) -> MLDataColumn<Element>](./subscript%28_%29-pp34.md)
  Creates a subset of the column, given a range of elements.
- [subscript<R>(R) -> MLDataColumn<Element>](./subscript%28_%29-5mczv.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLDataColumn<Element>](./prefix%28_%29.md)
  Creates a subset of the column, given a number of initial elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/suffix(_:))*