# NSCollectionLayoutAnchor

**Framework**: AppKit  
**Kind**: class

An object that defines how to attach a supplementary item to an item in a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSCollectionLayoutAnchor
```

#### Overview

You use an anchor to attach a supplementary item to a specific item. An anchor contains information about where on the item your supplementary item is attached, including:

- An edge or set of edges. You can attach a supplementary item to a single edge, or to a corner by specifying two adjacent edges.
- An offset from the item. By default, the supplementary item is anchored within the specified edges of the item it’s attached to. You can change this location by providing a custom offset when you create an anchor.

##### Edges

The leading and trailing edges for anchors differ in left-to-right versus right-to-left environments. In a left-to-right environment, the leading edge is on the left, and the trailing edge is on the right. In a right-to-left environment, the leading edge is on the right, and the trailing edge is on the left. This difference ensures that your collection view layout is built with support for right-to-left languages.

The following diagram shows anchor placement for the specified edges in a left-to-right environment.

![Diagram showing anchor positions. Top, bottom, leading, and trailing anchors are on the halfway point on their respective edges. The anchors defined by the edge combinations top and leading, top and trailing, bottom and leading, and bottom and trailing are in the corners between each of those sets of edges.](https://docs-assets.developer.apple.com/published/b7e68b458cab77379003c0ce5e2ef3e9/media-3570665%402x.png)

##### Offset

You can express anchor offset in these ways:

- Absolute value. The offset is calculated as a point value. For example, an absolute x offset of `30.0` means that the origin of the supplementary item is offset by 30 points in the positive x direction.
- Fractional value. The offset is calculated as a fraction of the supplementary item’s dimensions. For example, a fractional x offset of `0.3` means that the origin of the supplementary item is offset by 30% of the supplementary item’s width in the positive x direction.

The following code creates a basic badge and attaches it to an item’s top trailing corner.

## Topics

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge)](nscollectionlayoutanchor/init(edges:).md)
  Creates an anchor with the specified edges to attach to.
- [convenience init(edges: NSDirectionalRectEdge, absoluteOffset: NSPoint)](nscollectionlayoutanchor/init(edges:absoluteoffset:).md)
  Creates an anchor with the specified edges to attach to, offset by the provided absolute value.
- [convenience init(edges: NSDirectionalRectEdge, fractionalOffset: NSPoint)](nscollectionlayoutanchor/init(edges:fractionaloffset:).md)
  Creates an anchor with the specified edges to attach to, offset by the provided fractional value.
### Getting the edges
- [var edges: NSDirectionalRectEdge](nscollectionlayoutanchor/edges.md)
  The edges of the item an anchor is attached to.
### Getting the offset
- [var offset: NSPoint](nscollectionlayoutanchor/offset.md)
  The floating-point value of the anchor’s offset from the item it’s attached to.
- [var isAbsoluteOffset: Bool](nscollectionlayoutanchor/isabsoluteoffset.md)
  A Boolean value that indicates whether the anchor’s offset is expressed as an absolute value.
- [var isFractionalOffset: Bool](nscollectionlayoutanchor/isfractionaloffset.md)
  A Boolean value that indicates whether the anchor’s offset is expressed as a fraction of its supplementary item’s dimension.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.
- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutanchor)*