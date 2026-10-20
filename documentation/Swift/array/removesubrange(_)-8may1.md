# removeSubrange(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes the elements in the specified subrange from the collection.

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
mutating func removeSubrange(_ bounds: Range<Self.Index>)
```

#### Discussion

All the elements following the specified position are moved to close the gap. This example removes three elements from the middle of an array of measurements.

```swift
var measurements = [1.2, 1.5, 2.9, 1.2, 1.5]
measurements.removeSubrange(1..<4)
print(measurements)
// Prints "[1.2, 1.5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Complexity**: O(*n*), where *n* is the length of the collection.

## Parameters

- `bounds`: The range of the collection to be removed. The bounds of the range must be valid indices of the collection.

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
- [func removeSubrange<R>(R)](./removesubrange%28_%29-9twou.md)
  Removes the elements in the specified subrange from the collection.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29-5k61r.md)
  Removes all the elements that satisfy the given predicate.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all elements from the array.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/removesubrange(_:)-8may1)*