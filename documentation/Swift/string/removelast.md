# removeLast(_:)

**Framework**: Swift  
**Kind**: method

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

#### Discussion

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(), where  is the specified number of elements.

## Parameters

- `k`: The number of elements to remove from the collection.    must be greater than or equal to zero and must not exceed the   number of elements in the collection.

## See Also

- [func remove(at: String.Index) -> Character](string/remove(at:).md)
  Removes and returns the character at the specified position.
- [func remove(at: Self.Index) -> Self.Element](string/remove(at:)-5g0wm.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](string/removeall(keepingcapacity:).md)
  Replaces this string with the empty string.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](string/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](string/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](string/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](string/removelast.md)
  Removes and returns the last element of the collection.
- [func removeSubrange(Range<String.Index>)](string/removesubrange(_:).md)
  Removes the characters in the given range.
- [func removeSubrange(Range<Self.Index>)](string/removesubrange(_:)-8maxn.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](string/removesubrange(_:)-9twng.md)
  Removes the elements in the specified subrange from the collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](string/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](string/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](string/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](string/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popLast() -> Self.Element?](string/poplast.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/removelast(_:))*