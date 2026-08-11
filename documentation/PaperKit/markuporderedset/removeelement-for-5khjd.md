# removeElement(for:)

**Framework**: PaperKit  
**Kind**: method

Removes the associated element for the given id from the set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func removeElement(for id: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?
```

#### Return Value

The associated element for `id` if the set contains `id`; otherwise, `nil`.

## Parameters

- `id`: The id of the element to remove.

## See Also

- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/remove(_:).md)
  Removes the given element from the set.
- [func remove(at: Int) -> MarkupOrderedSet.Element](markuporderedset/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](markuporderedset/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](markuporderedset/removeelement(for:)-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](markuporderedset/removestroke(for:).md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/removeelement(for:)-5khjd)*