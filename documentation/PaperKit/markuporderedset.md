# MarkupOrderedSet

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

An ordered set of markup elements.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MarkupOrderedSet
```

#### Overview

The set ensures all elements have unique `id` values.

## Topics

### Creating a set
- [init()](./markuporderedset/init%28%29.md)
  Creates a new, empty collection.
### Adding elements
- [func append(MarkupOrderedSet.Element) -> (inserted: Bool, index: Int)](./markuporderedset/append%28_%29.md)
  Appends a new member to the end of the set, if the set doesn’t already contain it.
- [func append(contentsOf: some Sequence<any Markup>)](./markuporderedset/append%28contentsof%29.md)
  Appends the contents of a sequence to the end of the set, excluding elements that are already members.
- [func insert(MarkupOrderedSet.Element, at: Int) -> (inserted: Bool, index: Int)](./markuporderedset/insert%28_,at%29.md)
  Inserts a new member at the specified index, if the set doesn’t already contain it.
- [func updateOrAppend(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](./markuporderedset/updateorappend%28_%29.md)
  Adds the given element to the set unconditionally, either appending it to the set, or replacing an existing value if one with the same id is present.
### Accessing elements
- [subscript(UUID) -> PKStroke?](./markuporderedset/subscript%28_%29-1h73t.md)
  Accesses the stroke for the given id.
- [subscript<T>(MarkupID<T>) -> T?](./markuporderedset/subscript%28_%29-6e2ez.md)
  Accesses the element for the given id.
- [subscript(MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./markuporderedset/subscript%28_%29-79x8r.md)
  Accesses the element for the given id.
- [var ids: MarkupOrderedSet.ElementIDs](./markuporderedset/ids.md)
  A view of the set’s element ids.
- [var strokes: [PKStroke]](./markuporderedset/strokes.md)
  The strokes in the set.
- [var count: Int](./markuporderedset/count.md)
  The number of elements in the set.
### Removing elements
- [func remove(MarkupOrderedSet.Element) -> MarkupOrderedSet.Element?](./markuporderedset/remove%28_%29.md)
  Removes the given element from the set.
- [func remove(at: Int) -> MarkupOrderedSet.Element](./markuporderedset/remove%28at%29.md)
  Removes and returns the element at the specified position.
- [func removeAll(where: (MarkupOrderedSet.Element) throws -> Bool) rethrows](./markuporderedset/removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeElement<T>(for: MarkupID<T>) -> T?](./markuporderedset/removeelement%28for%29-4pqof.md)
  Removes the associated element for the given id from the set.
- [func removeElement(for: MarkupOrderedSet.ElementID) -> MarkupOrderedSet.Element?](./markuporderedset/removeelement%28for%29-5khjd.md)
  Removes the associated element for the given id from the set.
- [func removeStroke(for: UUID) -> PKStroke?](./markuporderedset/removestroke%28for%29.md)
  Removes the associated stroke for the given id from the set.
### Finding elements
- [func contains(MarkupOrderedSet.Element) -> Bool](./markuporderedset/contains%28_%29.md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func firstIndex(of: MarkupOrderedSet.Element) -> Int?](./markuporderedset/firstindex%28of%29.md)
  Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
### Identifying elements
- [MarkupOrderedSet.ElementID](./markuporderedset/elementid.md)
  The markup ID types supported in a markup ordered set.
- [MarkupOrderedSet.ElementIDs](./markuporderedset/elementids.md)
  A view of a set’s ids.
- [MarkupOrderedSet.Element](./markuporderedset/element.md)
  The type of element in the set.
### Default Implementations
- [BidirectionalCollection Implementations](./markuporderedset/bidirectionalcollection-implementations.md)
- [Collection Implementations](./markuporderedset/collection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Data model
- [struct PaperMarkup](./papermarkup.md)
  The data model object for storing markup data created from a `PaperViewController`.
- [struct MarkupID](./markupid.md)
  An opaque ID for markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset)*