# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes and returns the element at the specified position.

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
@discardableResult
mutating func remove(at index: Int) -> Element
```

#### Return Value

The element at the specified index.

#### Discussion

All the elements following the specified position are moved up to close the gap.

```swift
var measurements: [Double] = [1.1, 1.5, 2.9, 1.2, 1.5, 1.3, 1.2]
let removed = measurements.remove(at: 2)
print(measurements)
// Prints "[1.1, 1.5, 1.2, 1.5, 1.3, 1.2]"
```

> **Note**: O(), where  is the length of the array.

## Parameters

- `index`: The position of the element to remove.   must   be a valid index of the array.

## See Also

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
- [func popLast() -> Self.Element?](array/poplast.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/remove(at:))*