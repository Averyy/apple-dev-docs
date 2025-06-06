# suffix(_:)

**Framework**: Create ML  
**Kind**: method

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
func suffix(_ maxLength: Int = 10) -> MLUntypedColumn
```

#### Return Value

A new column.

## Parameters

- `maxLength`: The largest number of elements to use from the end of the   column. The default value is  .

## See Also

- [subscript(Range<Int>) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-33ua2.md)
  Creates a subset of the column, given a range of elements.
- [subscript<R>(R) -> MLUntypedColumn](mluntypedcolumn/subscript(_:)-9dpy7.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLUntypedColumn](mluntypedcolumn/prefix(_:).md)
  Creates a subset of the column, given a number of initial elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/suffix(_:))*