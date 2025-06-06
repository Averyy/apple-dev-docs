# isNil(at:)

**Framework**: TabularData  
**Kind**: method

Returns a Boolean that indicates whether the element at the index is missing.

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
func isNil(at index: Int) -> Bool
```

## Parameters

- `index`: An index.

## See Also

- [var name: String](discontiguouscolumnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](discontiguouscolumnslice/count.md)
  The number of elements in the column slice.
- [var wrappedElementType: any Any.Type](discontiguouscolumnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](discontiguouscolumnslice/argmin.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](discontiguouscolumnslice/argmax.md)
  Returns the index of the element with the highest value, ignoring missing elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/isnil(at:))*