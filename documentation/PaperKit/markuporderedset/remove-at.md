# remove(at:)

**Framework**: PaperKit  
**Kind**: method

Removes and returns the element at the specified position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func remove(at index: Int) -> MarkupOrderedSet.Element
```

#### Return Value

The removed element.

#### Discussion

The operation moves all elements following the specified position to close the resulting gap.

## Parameters

- `index`: The position of the element to remove. `index` must be a valid index of the collection that is not equal to the collection’s end index.

## See Also

- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/remove(_:).md)
  Removes the given element from the set.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](markuporderedset/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](markuporderedset/removeelement(for:)-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](markuporderedset/removeelement(for:)-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](markuporderedset/removestroke(for:).md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/remove(at:))*