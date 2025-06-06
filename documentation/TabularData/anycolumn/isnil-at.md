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

- `index`: The location of an element in the column.

## See Also

- [var name: String](anycolumn/name.md)
  The name of the column.
- [var count: Int](anycolumn/count.md)
  The number of elements in the column.
- [var missingCount: Int](anycolumn/missingcount.md)
  The number of missing elements in the column.
- [var wrappedElementType: any Any.Type](anycolumn/wrappedelementtype.md)
  The underlying type of the column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/isnil(at:))*