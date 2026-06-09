# remove(_:)

**Framework**: PaperKit  
**Kind**: method

Removes the given element from the set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func remove(_ member: MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?
```

#### Return Value

The element equal to `member` if `member` is contained in the set; otherwise, `nil`.

## Parameters

- `member`: The element of the set to remove.

## See Also

- [func remove(at: Int) -> MarkupOrderedSet.Element](markuporderedset/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](markuporderedset/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](markuporderedset/removeelement(for:)-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](markuporderedset/removeelement(for:)-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](markuporderedset/removestroke(for:).md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/remove(_:))*