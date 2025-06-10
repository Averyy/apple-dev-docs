# removeLast(_:)

**Framework**: TabularData  
**Kind**: method

Removes the given number of elements from the end of the collection.

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
mutating func removeLast(_ k: Int)
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to remove.

## Parameters

- `k`: The number of elements to remove.   must be greater   than or equal to zero, and must be less than or equal to the number of   elements in the collection.

## See Also

- [func popFirst() -> Self.Element?](columnslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func popLast() -> Self.Element?](columnslice/poplast.md)
  Removes and returns the last element of the collection.
- [func removeFirst() -> Self.Element](columnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](columnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](columnslice/removelast.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/removelast(_:))*