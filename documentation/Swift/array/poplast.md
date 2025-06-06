# popLast()

**Framework**: Swift  
**Kind**: method

Removes and returns the last element of the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func popLast() -> Self.Element?
```

#### Return Value

The last element of the collection if the collection is not empty; otherwise, `nil`.

#### Discussion

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(1)

O(1)

## See Also

- [func remove(at: Int) -> Element](array/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeFirst() -> Self.Element](array/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](array/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](array/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](array/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](array/removesubrange(_:)-8may1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](array/removesubrange(_:)-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](array/removeall(where:)-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(keepingCapacity: Bool)](array/removeall(keepingcapacity:).md)
  Removes all elements from the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/poplast())*