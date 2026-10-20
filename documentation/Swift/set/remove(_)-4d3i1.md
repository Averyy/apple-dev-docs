# remove(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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

Available when `Element` is `AnyHashable`.

## See Also

### Removing Elements
- [func filter<E>((Element) throws(E) -> Bool) throws(E) -> Set<Element>](./filter%28_%29.md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](./remove%28_%29-8p2tv.md)
  Removes the specified element from the set.
- [func removeFirst() -> Element](./removefirst%28%29.md)
  Removes the first element of the set.
- [func remove(at: Set<Element>.Index) -> Element](./remove%28at%29.md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/remove(_:)-4d3i1)*