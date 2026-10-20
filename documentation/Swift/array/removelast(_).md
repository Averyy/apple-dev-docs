# removeLast(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes the specified number of elements from the end of the collection.

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
mutating func removeLast(_ k: Int)
```

Available when `Self` conforms to `BidirectionalCollection`.

#### Discussion

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Complexity**: O(*k*), where *k* is the specified number of elements.

## Parameters

- `k`: The number of elements to remove from the collection. `k` must be greater than or equal to zero and must not exceed the number of elements in the collection.

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
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-8may1.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all elements from the array.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/removelast(_:))*