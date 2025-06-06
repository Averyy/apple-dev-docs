# removeFirst(_:)

**Framework**: Swift  
**Kind**: method

Removes the specified number of elements from the beginning of the collection.

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
mutating func removeFirst(_ k: Int)
```

#### Discussion

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeFirst(3)
print(bugs)
// Prints "["Damselfly", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `k`: The number of elements to remove from the collection.    must be greater than or equal to zero and must not exceed the   number of elements in the collection.

## See Also

- [func remove(at: Int) -> Element](array/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeFirst() -> Self.Element](array/removefirst.md)
  Removes and returns the first element of the collection.
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
- [func popLast() -> Self.Element?](array/poplast.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/removefirst(_:))*