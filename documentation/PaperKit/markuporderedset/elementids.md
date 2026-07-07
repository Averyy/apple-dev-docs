# MarkupOrderedSet.ElementIDs

**Framework**: PaperKit  
**Kind**: struct

A view of a set’s ids.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ElementIDs
```

## Topics

### Instance Properties
- [var endIndex: MarkupOrderedSet.ElementIDs.Index](markuporderedset/elementids/endindex.md)
  The index past the last element ID.
- [var startIndex: MarkupOrderedSet.ElementIDs.Index](markuporderedset/elementids/startindex.md)
  The index of the first element ID.
### Instance Methods
- [func index(after: MarkupOrderedSet.ElementIDs.Index) -> MarkupOrderedSet.ElementIDs.Index](markuporderedset/elementids/index(after:).md)
  Returns the index after the given index.
### Subscripts
- [subscript(MarkupOrderedSet.ElementIDs.Index) -> MarkupOrderedSet.ElementIDs.Element](markuporderedset/elementids/subscript(_:).md)
  Accesses the element ID at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [MarkupOrderedSet.ElementID](markuporderedset/elementid.md)
  The markup ID types supported in a markup ordered set.
- [MarkupOrderedSet.Element](markuporderedset/element.md)
  The type of element in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/elementids)*