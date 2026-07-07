# removeAll(where:)

**Framework**: PaperKit  
**Kind**: method

Removes all the elements that satisfy the given predicate.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func removeAll(where shouldBeRemoved: (MarkupOrderedSet.Element) throws -> Bool) rethrows
```

## Parameters

- `shouldBeRemoved`: A closure that takes an element of the set as its argument and returns a Boolean value indicating whether to remove the element from the set.

## See Also

- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/remove(_:).md)
  Removes the given element from the set.
- [func remove(at: Int) -> MarkupOrderedSet.Element](markuporderedset/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeElement<T>(for: MarkupID<T>) -> T?](markuporderedset/removeelement(for:)-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](markuporderedset/removeelement(for:)-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](markuporderedset/removestroke(for:).md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/removeall(where:))*