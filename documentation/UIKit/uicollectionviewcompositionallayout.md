# UICollectionViewCompositionalLayout

**Framework**: UIKit  
**Kind**: class

A layout object that lets you combine items in highly adaptive and flexible visual arrangements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewCompositionalLayout
```

#### Overview

A compositional layout is a type of collection view layout. It’s designed to be composable, flexible, and fast, letting you build any kind of visual arrangement for your content by combining — or compositing — each smaller component into a full layout.

A compositional layout is composed of one or more sections that break up the layout into distinct visual groupings. Each section is composed of groups of individual items, the smallest unit of data you want to present. A group might lay out its items in a horizontal row, a vertical column, or a custom arrangement.

![Schematic representation of the App Store app on iOS, showing a collection view with a compositional layout. The layout is composed of two horizontally-scrolling sections that have different layouts. The top section shows one group with one item visible onscreen, with other groups peeking in from the side of the screen. The bottom section shows one group that’s a column of three cells, each of those cells being an item. Each of the items, groups, and sections are outlined and labeled to show how the pieces fit together.](https://docs-assets.developer.apple.com/published/1bcae7456df55cf8e3407bb9324c0d33/media-3568664%402x.png)

You combine the components by building up from items into a group, from groups into a section, and finally into a full layout, like in this example of a basic list layout:

## Topics

### Creating a layout
- [init(section: NSCollectionLayoutSection)](uicollectionviewcompositionallayout/init(section:).md)
  Creates a compositional layout object with a single section.
- [init(section: NSCollectionLayoutSection, configuration: UICollectionViewCompositionalLayoutConfiguration)](uicollectionviewcompositionallayout/init(section:configuration:).md)
  Creates a compositional layout object with a single section and an additional configuration.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider)](uicollectionviewcompositionallayout/init(sectionprovider:).md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider, configuration: UICollectionViewCompositionalLayoutConfiguration)](uicollectionviewcompositionallayout/init(sectionprovider:configuration:).md)
  Creates a compositional layout object with a section provider and an additional configuration.
### Creating a list layout
- [static func list(using: UICollectionLayoutListConfiguration) -> UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout/list(using:).md)
  Creates a compositional layout that contains only list sections of the specified configuration.
- [struct UICollectionLayoutListConfiguration](uicollectionlayoutlistconfiguration-swift.struct.md)
  A configuration for creating a list layout.
### Configuring the layout
- [var configuration: UICollectionViewCompositionalLayoutConfiguration](uicollectionviewcompositionallayout/configuration.md)
  The layout’s configuration, such as its scroll direction and section spacing.

## Relationships

### Inherits From
- [UICollectionViewLayout](uicollectionviewlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout)*