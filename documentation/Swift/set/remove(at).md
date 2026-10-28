# remove(at:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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

Available when `Element` conforms to `Hashable`.

## Return Value

The element that was removed from the set.

## Parameters

- `position`: The index of the member to remove. `position` must be a valid index of the set, and must not be equal to the set’s end index.

## See Also

### Removing Elements
- [func filter<E>((Element) throws(E) -> Bool) throws(E) -> Set<Element>](./filter%28_%29.md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove(Element) -> Element?](./remove%28_%29-8p2tv.md)
  Removes the specified element from the set.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](./remove%28_%29-4d3i1.md)
- [func removeFirst() -> Element](./removefirst%28%29.md)
  Removes the first element of the set.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/remove(at:))*