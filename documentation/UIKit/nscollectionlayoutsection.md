# NSCollectionLayoutSection

**Framework**: UIKit  
**Kind**: class

A container that combines a set of groups into distinct visual groupings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutSection
```

#### Overview

A collection view layout has one or more sections. Sections provide a way to separate the layout into distinct pieces.

Each section can have the same layout or a different layout than the other sections in the collection view. A section’s layout is determined by the properties of the group ([`NSCollectionLayoutGroup`](nscollectionlayoutgroup.md)) that’s used to create the section.

In the Photos app, each section in the Years page uses the same layout. In the App Store, the Apps page displays several sections with different content arrangements.

![Schematic representation of the App Store app on iOS, showing a collection view with a compositional layout. The layout is composed of two horizontally-scrolling sections that have different layouts. The top section shows one group with one item visible onscreen, with other groups peeking in from the sides of the screen. The bottom section shows one group that’s a column of three cells, each of those cells being an item. The two different sections are highlighted and labeled as sections.](https://docs-assets.developer.apple.com/published/3a145ace5c9cd5a165dbc9c2759c035f/media-3568661%402x.png)

Each section can have its own background, header, and footer to distinguish it from other sections.

## Topics

### Creating a section
- [convenience init(group: NSCollectionLayoutGroup)](nscollectionlayoutsection/init(group:).md)
  Creates a section containing the specified group.
- [static func list(using: UICollectionLayoutListConfiguration, layoutEnvironment: any NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection](nscollectionlayoutsection/list(using:layoutenvironment:).md)
  Creates a list section with the specified list configuration and layout environment.
- [class func orthogonalLayoutSectionForMediaItems() -> NSCollectionLayoutSection](nscollectionlayoutsection/orthogonallayoutsectionformediaitems.md)
  Creates an orthogonally scrolling section with system default spacing.
### Specifying scrolling behavior
- [var orthogonalScrollingBehavior: UICollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsection/orthogonalscrollingbehavior.md)
  The section’s scrolling behavior in relation to the main layout axis.
- [var orthogonalScrollingProperties: UICollectionLayoutSectionOrthogonalScrollingProperties](nscollectionlayoutsection/orthogonalscrollingproperties.md)
  The section’s orthogonal scrolling properties.
- [class UICollectionLayoutSectionOrthogonalScrollingProperties](uicollectionlayoutsectionorthogonalscrollingproperties.md)
  An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.
### Configuring section spacing
- [var interGroupSpacing: CGFloat](nscollectionlayoutsection/intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutsection/contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var contentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [var supplementaryContentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/supplementarycontentinsetsreference.md)
  The reference boundary for content insets on boundary supplementary items.
- [enum UIContentInsetsReference](uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.
### Configuring additional views
- [var boundarySupplementaryItems: [NSCollectionLayoutBoundarySupplementaryItem]](nscollectionlayoutsection/boundarysupplementaryitems.md)
  An array of the supplementary items that are associated with the boundary edges of the section, such as headers and footers.
- [var decorationItems: [NSCollectionLayoutDecorationItem]](nscollectionlayoutsection/decorationitems.md)
  An array of the decoration items that are anchored to the section, such as background decoration views.
### Rendering items
- [var visibleItemsInvalidationHandler: NSCollectionLayoutSectionVisibleItemsInvalidationHandler?](nscollectionlayoutsection/visibleitemsinvalidationhandler.md)
  A closure called before each layout cycle to allow modification of the items in the section immediately before they’re displayed.
### Deprecated
- [var supplementariesFollowContentInsets: Bool](nscollectionlayoutsection/supplementariesfollowcontentinsets.md)
  A Boolean value that indicates whether the section’s supplementary items follow the specified content insets for the section.

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

- [class NSCollectionLayoutItem](nscollectionlayoutitem.md)
  The most basic component of a collection view’s layout.
- [class NSCollectionLayoutGroup](nscollectionlayoutgroup.md)
  A container for a set of items that lays out the items along a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection)*