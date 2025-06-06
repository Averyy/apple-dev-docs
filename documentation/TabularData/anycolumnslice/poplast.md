# popLast()

**Framework**: TabularData  
**Kind**: method

Removes and returns the last element of the collection.

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
mutating func popLast() -> Self.Element?
```

#### Return Value

The last element of the collection if the collection has one or more elements; otherwise, `nil`.

#### Discussion

You can use `popLast()` to remove the last element of a collection that might be empty. The `removeLast()` method must be used only on a nonempty collection.

> **Note**: O(1)

O(1)

## See Also

- [func popFirst() -> Self.Element?](anycolumnslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst() -> Self.Element](anycolumnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](anycolumnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](anycolumnslice/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](anycolumnslice/removelast(_:).md)
  Removes the given number of elements from the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/poplast())*