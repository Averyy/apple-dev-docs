# removeAll(where:)

**Framework**: Swift  
**Kind**: method

Removes all the elements that satisfy the given predicate.

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
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

#### Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the vowels from a string:

```swift
var phrase = "The rain in Spain stays mainly in the plain."

let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
phrase.removeAll(where: { vowels.contains($0) })
// phrase == "Th rn n Spn stys mnly n th pln."
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `shouldBeRemoved`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be removed from the collection.

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
- [func removeAll(keepingCapacity: Bool)](array/removeall(keepingcapacity:).md)
  Removes all elements from the array.
- [func popLast() -> Self.Element?](array/poplast.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/removeall(where:)-5k61r)*