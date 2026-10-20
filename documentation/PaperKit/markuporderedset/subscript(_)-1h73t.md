# subscript(_:)

**Framework**: PaperKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the stroke for the given id.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
subscript(id: UUID) -> PKStroke? { get set }
```

## See Also

### Accessing elements
- [subscript<T>(MarkupID<T>) -> T?](./subscript%28_%29-6e2ez.md)
  Accesses the element for the given id.
- [subscript(MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./subscript%28_%29-79x8r.md)
  Accesses the element for the given id.
- [var ids: MarkupOrderedSet.ElementIDs](./ids.md)
  A view of the set’s element ids.
- [var strokes: [PKStroke]](./strokes.md)
  The strokes in the set.
- [var count: Int](./count.md)
  The number of elements in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/subscript(_:)-1h73t)*