# remove(at:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Removes and returns the element at the specified position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
mutating func remove(at index: Int) -> MarkupOrderedSet.Element
```

## Return Value

The removed element.

## Discussion

The operation moves all elements following the specified position to close the resulting gap.

## Parameters

- `index`: The position of the element to remove. `index` must be a valid index of the collection that is not equal to the collection’s end index.

## See Also

### Removing elements
- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](./remove%28_%29.md)
  Removes the given element from the set.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](./removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](./removeelement%28for%29-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./removeelement%28for%29-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](./removestroke%28for%29.md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/remove(at:))*