# subscript(_:)

**Framework**: PaperKit  
**Kind**: subscript

Accesses the stroke for the given id.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(id: UUID) -> PKStroke? { get set }
```

## See Also

- [subscript<T>(MarkupID<T>) -> T?](markuporderedset/subscript(_:)-6e2ez.md)
  Accesses the element for the given id.
- [subscript(MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](markuporderedset/subscript(_:)-79x8r.md)
  Accesses the element for the given id.
- [var ids: MarkupOrderedSet.ElementIDs](markuporderedset/ids.md)
  A view of the set’s element ids.
- [var strokes: [PKStroke]](markuporderedset/strokes.md)
  The strokes in the set.
- [var count: Int](markuporderedset/count.md)
  The number of elements in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/subscript(_:)-1h73t)*