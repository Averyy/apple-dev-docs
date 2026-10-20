# removeAll(where:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Removes all the elements that satisfy the given predicate.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func removeAll(where shouldBeRemoved: (MarkupOrderedSet.Element) throws -> Bool) rethrows
```

## Parameters

- `shouldBeRemoved`: A closure that takes an element of the set as its argument and returns a Boolean value indicating whether to remove the element from the set.

## See Also

### Removing elements
- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](./remove%28_%29.md)
  Removes the given element from the set.
- [func remove(at: Int) -> MarkupOrderedSet.Element](./remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func removeElement<T>(for: MarkupID<T>) -> T?](./removeelement%28for%29-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./removeelement%28for%29-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](./removestroke%28for%29.md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/removeall(where:))*