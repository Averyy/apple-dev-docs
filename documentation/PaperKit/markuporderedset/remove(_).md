# remove(_:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Removes the given element from the set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
mutating func remove(_ member: MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?
```

## Return Value

The element equal to `member` if `member` is contained in the set; otherwise, `nil`.

## Parameters

- `member`: The element of the set to remove.

## See Also

### Removing elements
- [func remove(at: Int) -> MarkupOrderedSet.Element](./remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](./removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](./removeelement%28for%29-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./removeelement%28for%29-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](./removestroke%28for%29.md)
  Removes the associated stroke for the given id from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/remove(_:))*