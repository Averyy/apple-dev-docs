# UICollectionLayoutListConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration for creating a list layout.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICollectionLayoutListConfiguration : NSObject
```

#### Overview

Use this configuration to create a list section for a compositional layout ([`UICollectionViewCompositionalLayout`](./uicollectionviewcompositionallayout.md)), or a layout containing only list sections. The following example shows how to create a compositional layout that contains only list sections by applying the same configuration to each section in the list layout:

```objc
UICollectionLayoutListConfiguration *configuration = [[UICollectionLayoutListConfiguration alloc] initWithAppearance:UICollectionLayoutListAppearanceSidebar];
UICollectionViewCompositionalLayout *layout = [UICollectionViewCompositionalLayout layoutWithListConfiguration:configuration];
```

To implement different list configurations for different sections, use a compositional layout’s section provider to create each section with its own list configuration.

```objc
UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSectionProvider:^NSCollectionLayoutSection *(NSInteger sectionIndex, id<NSCollectionLayoutEnvironment> layoutEnvironment) {
    UICollectionLayoutListConfiguration *configuration = [[UICollectionLayoutListConfiguration alloc] initWithAppearance:UICollectionLayoutListAppearanceInsetGrouped];
    UICollectionLayoutListHeaderMode mode = (sectionIndex == 0) ? UICollectionLayoutListHeaderModeSupplementary : UICollectionLayoutListHeaderModeNone;
    [configuration setHeaderMode:mode];
    NSCollectionLayoutSection *section = [NSCollectionLayoutSection sectionWithListConfiguration:configuration layoutEnvironment:layoutEnvironment];
    return section;
}];
```

## Topics

### Creating a list layout configuration
- [- initWithAppearance:](./uicollectionlayoutlistconfiguration-c.class/initwithappearance_.md)
  Creates a list layout configuration with the specified appearance.
### Configuring appearance
- [appearance](./uicollectionlayoutlistconfiguration-c.class/appearance.md)
  The overall appearance of the list layout.
- [backgroundColor](./uicollectionlayoutlistconfiguration-c.class/backgroundcolor.md)
  The background color of the list.
- [UICollectionLayoutListAppearance](./uicollectionlayoutlistappearance.md)
  Constants that describe the appearance of the list.
### Configuring separators
- [showsSeparators](./uicollectionlayoutlistconfiguration-c.class/showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](./uicollectionlayoutlistconfiguration-c.class/separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](./uilistseparatorconfiguration-c.class.md)
  A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](./uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler.md)
  The closure that provides granular control over the list separator appearance of each item.
- [UICollectionLayoutListItemSeparatorHandler](./uicollectionlayoutlistitemseparatorhandler.md)
  A closure that provides granular control over list separator appearance.
### Configuring headers and footers
- [headerMode](./uicollectionlayoutlistconfiguration-c.class/headermode.md)
  The type of header to use for the list.
- [footerMode](./uicollectionlayoutlistconfiguration-c.class/footermode.md)
  The type of footer to use for the list.
- [UICollectionLayoutListHeaderMode](./uicollectionlayoutlistheadermode.md)
  Constants that describe the list’s header mode.
- [UICollectionLayoutListFooterMode](./uicollectionlayoutlistfootermode.md)
  Constants that describe the list’s footer mode.
- [headerTopPadding](./uicollectionlayoutlistconfiguration-c.class/headertoppadding.md)
  The amount of padding above each section header.
- [UICollectionViewLayoutAutomaticDimension](./uicollectionviewlayoutautomaticdimension.md)
  A constant that specifies a default value for a particular dimension.
### Customizing swipe actions
- [leadingSwipeActionsConfigurationProvider](./uicollectionlayoutlistconfiguration-c.class/leadingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [trailingSwipeActionsConfigurationProvider](./uicollectionlayoutlistconfiguration-c.class/trailingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the trailing edge of the cell.
- [UICollectionLayoutListSwipeActionsConfigurationProvider](./uicollectionlayoutlistswipeactionsconfigurationprovider.md)
  A closure that configures the swipe actions for a cell.
### Managing content-hugging behavior
- [contentHuggingElements](./uicollectionlayoutlistconfiguration-c.class/contenthuggingelements.md)
  A setting that determines which type of items tightly hug their content.
- [UICollectionLayoutListContentHuggingElements](./uicollectionlayoutlistcontenthuggingelements.md)
  Constants that determine which types of items in a collection view tightly hug their content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Related Documentation
- [+ sectionWithListConfiguration:layoutEnvironment:](./nscollectionlayoutsection/sectionwithlistconfiguration_layoutenvironment_.md)
  Creates a list section with the specified list configuration and layout environment.
### Creating a list layout
- [+ layoutWithListConfiguration:](./uicollectionviewcompositionallayout/layoutwithlistconfiguration_.md)
  Creates a compositional layout that contains only list sections of the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class)*