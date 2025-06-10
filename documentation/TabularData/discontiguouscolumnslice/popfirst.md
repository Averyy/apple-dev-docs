# popFirst()

**Framework**: TabularData  
**Kind**: method

Removes and returns the first element of the collection.

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
mutating func popFirst() -> Self.Element?
```

#### Return Value

The first element of the collection if the collection is not empty; otherwise, `nil`.

#### Discussion

> **Note**: O(1)

## See Also

- [func popLast() -> Self.Element?](discontiguouscolumnslice/poplast.md)
  Removes and returns the last element of the collection.
- [func removeFirst() -> Self.Element](discontiguouscolumnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](discontiguouscolumnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](discontiguouscolumnslice/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](discontiguouscolumnslice/removelast(_:).md)
  Removes the given number of elements from the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/popfirst())*