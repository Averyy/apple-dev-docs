# firstIndex(of:)

**Framework**: TabularData  
**Kind**: method

Returns the first index where the specified value appears in the collection.

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
func firstIndex(of element: Self.Element) -> Self.Index?
```

#### Return Value

The first index where `element` is found. If `element` is not found in the collection, returns `nil`.

#### Discussion

After using `firstIndex(of:)` to find the position of a particular element in a collection, you can use it to access the element by subscripting. This example shows how you can modify one of the names in an array of students.

```None
var students = ["Ben", "Ivy", "Jordell", "Maxime"]
if let i = students.firstIndex(of: "Maxime") {
    students[i] = "Max"
}
print(students)
// Prints "["Ben", "Ivy", "Jordell", "Max"]"
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `element`: An element to search for in the collection.

## See Also

- [var indices: DefaultIndices<Self>](filledcolumn/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](filledcolumn/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](filledcolumn/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](filledcolumn/index(_:offsetby:limitedby:).md)
- [func formIndex(inout Self.Index, offsetBy: Int)](filledcolumn/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](filledcolumn/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(of: Self.Element) -> Self.Index?](filledcolumn/index(of:).md)
  Returns the first index where the specified value appears in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/firstindex(of:))*