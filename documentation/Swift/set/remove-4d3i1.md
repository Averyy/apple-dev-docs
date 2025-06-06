# remove(_:)

**Framework**: Swift  
**Kind**: method

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
mutating func remove<ConcreteElement>(_ member: ConcreteElement) -> ConcreteElement? where ConcreteElement : Hashable
```

## See Also

- [func filter((Element) throws -> Bool) rethrows -> Set<Element>](set/filter(_:).md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](set/remove(_:)-8p2tv.md)
  Removes the specified element from the set.
- [func removeFirst() -> Element](set/removefirst.md)
  Removes the first element of the set.
- [func remove(at: Set<Element>.Index) -> Element](set/remove(at:).md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/remove(_:)-4d3i1)*