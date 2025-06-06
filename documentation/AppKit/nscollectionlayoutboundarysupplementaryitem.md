# NSCollectionLayoutBoundarySupplementaryItem

**Framework**: AppKit  
**Kind**: class

An object used to add headers or footers to a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutBoundarySupplementaryItem
```

#### Overview

A boundary supplementary item is a specialized type of supplementary item ([`NSCollectionLayoutSupplementaryItem`](nscollectionlayoutsupplementaryitem.md)). You use boundary supplementary items to add headers or footers to a section of a collection view or the entire collection view.

Each type of supplementary item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

Add boundary supplementary items to a section by setting that section’s [`boundarySupplementaryItems`](nscollectionviewcompositionallayoutconfiguration/boundarysupplementaryitems.md) property:

## Topics

### Creating a boundary supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment)](nscollectionlayoutboundarysupplementaryitem/init(layoutsize:elementkind:alignment:).md)
  Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout.
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, alignment: NSRectAlignment, absoluteOffset: NSPoint)](nscollectionlayoutboundarysupplementaryitem/init(layoutsize:elementkind:alignment:absoluteoffset:).md)
  Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout at an absolute offset.
### Specifying scrolling behavior
- [var pinToVisibleBounds: Bool](nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds.md)
  A Boolean value that indicates whether a header or footer is pinned to the top or bottom visible boundary of the section or layout it’s attached to.
### Specifying position
- [var offset: NSPoint](nscollectionlayoutboundarysupplementaryitem/offset.md)
  The floating-point value of the boundary supplementary item’s offset from the section or layout it’s attached to.
- [var alignment: NSRectAlignment](nscollectionlayoutboundarysupplementaryitem/alignment.md)
  The alignment of the boundary supplementary item relative to the section or layout it’s attached to.
- [var extendsBoundary: Bool](nscollectionlayoutboundarysupplementaryitem/extendsboundary.md)
  A Boolean value that indicates whether a boundary supplementary item extends the content area of the section or layout it’s attached to.

## Relationships

### Inherits From
- [NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.
- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutboundarysupplementaryitem)*