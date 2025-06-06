# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes the element at the given index of the set.

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
mutating func remove(at position: Set<Element>.Index) -> Element
```

#### Return Value

The element that was removed from the set.

## Parameters

- `position`: The index of the member to remove.   must   be a valid index of the set, and must not be equal to the set’s end   index.

## See Also

- [func filter((Element) throws -> Bool) rethrows -> Set<Element>](set/filter(_:).md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](set/remove(_:)-8p2tv.md)
  Removes the specified element from the set.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](set/remove(_:)-4d3i1.md)
- [func removeFirst() -> Element](set/removefirst.md)
  Removes the first element of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/remove(at:))*