# count

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The number of elements in the column slice.

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
var count: Int { get }
```

## See Also

### Inspecting a Column Slice
- [var name: String](./name.md)
  The name of the slice’s parent column.
- [var wrappedElementType: any Any.Type](./wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](./argmin%28%29.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](./argmax%28%29.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](./isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at an index is missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/count)*