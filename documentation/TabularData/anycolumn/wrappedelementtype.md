# wrappedElementType

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The underlying type of the column’s elements.

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
var wrappedElementType: any Any.Type { get }
```

## See Also

### Inspecting a Type-Erased Column
- [var name: String](./name.md)
  The name of the column.
- [var count: Int](./count.md)
  The number of elements in the column.
- [var missingCount: Int](./missingcount.md)
  The number of missing elements in the column.
- [func isNil(at: Int) -> Bool](./isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at the index is missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/wrappedelementtype)*