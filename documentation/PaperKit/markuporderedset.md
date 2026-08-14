# MarkupOrderedSet

**Framework**: PaperKit  
**Kind**: struct

An ordered set of markup elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MarkupOrderedSet
```

#### Overview

The set ensures all elements have unique `id` values.

## Topics

### Creating a set
- [init()](markuporderedset/init.md)
  Creates a new, empty collection.
### Adding elements
- [func append(MarkupOrderedSet.Element) -> (inserted: Bool, index: Int)](markuporderedset/append(_:).md)
  Appends a new member to the end of the set, if the set doesn’t already contain it.
- [func append(contentsOf: some Sequence<any Markup>)](markuporderedset/append(contentsof:).md)
  Appends the contents of a sequence to the end of the set, excluding elements that are already members.
- [func insert(MarkupOrderedSet.Element, at: Int) -> (inserted: Bool, index: Int)](markuporderedset/insert(_:at:).md)
  Inserts a new member at the specified index, if the set doesn’t already contain it.
- [func updateOrAppend(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/updateorappend(_:).md)
  Adds the given element to the set unconditionally, either appending it to the set, or replacing an existing value if one with the same id is present.
### Accessing elements
- [subscript(UUID) -> PKStroke?](markuporderedset/subscript(_:)-1h73t.md)
  Accesses the stroke for the given id.
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
### Removing elements
- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](markuporderedset/remove(_:).md)
  Removes the given element from the set.
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
### Finding elements
- [func contains(MarkupOrderedSet.Element) -> Bool](markuporderedset/contains(_:).md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func firstIndex(of: MarkupOrderedSet.Element) -> Int?](markuporderedset/firstindex(of:).md)
  Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
### Identifying elements
- [MarkupOrderedSet.ElementID](markuporderedset/elementid.md)
  The markup ID types supported in a markup ordered set.
- [MarkupOrderedSet.ElementIDs](markuporderedset/elementids.md)
  A view of a set’s ids.
- [MarkupOrderedSet.Element](markuporderedset/element.md)
  The type of element in the set.
### Default Implementations
- [BidirectionalCollection Implementations](markuporderedset/bidirectionalcollection-implementations.md)
- [Collection Implementations](markuporderedset/collection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [struct PaperMarkup](papermarkup.md)
  The data model object for storing markup data created from a `PaperViewController`.
- [struct MarkupID](markupid.md)
  An opaque ID for markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset)*