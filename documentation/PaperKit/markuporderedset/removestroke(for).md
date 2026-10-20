# removeStroke(for:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Removes the associated stroke for the given id from the set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
mutating func removeStroke(for id: UUID) -> PKStroke?
```

#### Return Value

The associated stroke for `id` if the set contains `id`; otherwise, `nil`.

## Parameters

- `id`: The id of the stroke to remove.

## See Also

### Removing elements
- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](./remove%28_%29.md)
  Removes the given element from the set.
- [func remove(at: Int) -> MarkupOrderedSet.Element](./remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](./removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](./removeelement%28for%29-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./removeelement%28for%29-5khjd.md)
  Removes the associated element for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/removestroke(for:))*