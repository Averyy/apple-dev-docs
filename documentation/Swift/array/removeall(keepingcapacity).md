# removeAll(keepingCapacity:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes all elements from the array.

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
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

## Discussion

> **Complexity**: O(*n*), where *n* is the length of the array.

## Parameters

- `keepCapacity`: Pass `true` to keep the existing capacity of the array after removing its elements. The default value is `false`.

## See Also

### Removing Elements
- [func remove(at: Int) -> Element](./remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func removeFirst() -> Self.Element](./removefirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./removefirst%28_%29.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-8may1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/removeall(keepingcapacity:))*