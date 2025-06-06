# NSCollectionLayoutContainer

**Framework**: AppKit  
**Kind**: protocol

A protocol used to provide information about the size and content insets of a layout’s container.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
protocol NSCollectionLayoutContainer : NSObjectProtocol
```

#### Overview

In a section provider, you use the [`container`](nscollectionlayoutenvironment/container.md) property of the layout environment ([`NSCollectionLayoutEnvironment`](nscollectionlayoutenvironment.md)) to get information about the container of the layout, such as its size and content insets. Knowing about the container’s size while rendering the layout’s sections helps you make decisions about how to display the layout.

## Topics

### Getting content size
- [var contentSize: NSSize](nscollectionlayoutcontainer/contentsize.md)
  The size of the container before content insets are applied.
- [var effectiveContentSize: NSSize](nscollectionlayoutcontainer/effectivecontentsize.md)
  The size of the container after content insets are applied.
### Getting content insets
- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutcontainer/contentinsets.md)
  The amount of space added around the content of the container to adjust its final size.
- [var effectiveContentInsets: NSDirectionalEdgeInsets](nscollectionlayoutcontainer/effectivecontentinsets.md)
  The amount of space added around the content of the container to adjust its final size after item content insets are applied.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCollectionLayoutDimension](nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSize](nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutSpacing](nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [class NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutcontainer)*