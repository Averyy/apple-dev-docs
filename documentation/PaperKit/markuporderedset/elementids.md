# MarkupOrderedSet.ElementIDs

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

A view of a set’s ids.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ElementIDs
```

## Topics

### Instance Properties
- [var endIndex: MarkupOrderedSet.ElementIDs.Index](./elementids/endindex.md)
  The index past the last element ID.
- [var startIndex: MarkupOrderedSet.ElementIDs.Index](./elementids/startindex.md)
  The index of the first element ID.
### Instance Methods
- [func index(after: MarkupOrderedSet.ElementIDs.Index) -> MarkupOrderedSet.ElementIDs.Index](./elementids/index%28after%29.md)
  Returns the index after the given index.
### Subscripts
- [subscript(MarkupOrderedSet.ElementIDs.Index) -> MarkupOrderedSet.ElementIDs.Element](./elementids/subscript%28_%29.md)
  Accesses the element ID at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Identifying elements
- [MarkupOrderedSet.ElementID](./elementid.md)
  The markup ID types supported in a markup ordered set.
- [MarkupOrderedSet.Element](./element.md)
  The type of element in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/elementids)*