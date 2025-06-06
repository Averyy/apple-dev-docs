# removeFirst()

**Framework**: Swift  
**Kind**: method

Removes the first element of the set.

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
mutating func removeFirst() -> Element
```

#### Return Value

A member of the set.

#### Discussion

Because a set is not an ordered collection, the “first” element may not be the first element that was added to the set. The set must not be empty.

> **Note**: Amortized O(1) if the set does not wrap a bridged `NSSet`. If the set wraps a bridged `NSSet`, the performance is unspecified.

## See Also

- [func filter((Element) throws -> Bool) rethrows -> Set<Element>](set/filter(_:).md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](set/remove(_:)-8p2tv.md)
  Removes the specified element from the set.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](set/remove(_:)-4d3i1.md)
- [func remove(at: Set<Element>.Index) -> Element](set/remove(at:).md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/removefirst())*