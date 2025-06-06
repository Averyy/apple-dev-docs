# name

**Framework**: TabularData  
**Kind**: property

The name of the slice’s parent column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var name: String { get set }
```

## See Also

- [var count: Int](columnslice/count.md)
  The number of elements in the column slice.
- [var wrappedElementType: any Any.Type](columnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](columnslice/argmin.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](columnslice/argmax.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](columnslice/isnil(at:).md)
  Returns a Boolean that indicates whether the element at an index is missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/name)*