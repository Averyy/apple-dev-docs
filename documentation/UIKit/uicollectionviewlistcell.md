# UICollectionViewListCell

**Framework**: UIKit  
**Kind**: class

A collection view cell that provides list features and default styling.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewListCell
```

#### Overview

A list cell represents an individual item that might appear in a list. List cells provide built-in support for indentation, and the ability to add cell accessories ([`UICellAccessory`](uicellaccessory-swift.struct.md)) for visual adornment or to support user interactions with the cell.

You can use a list cell in any type of layout. Using a list cell inside a list enables additional list-specific behavior for the cells. For example, in a list section or layout, you can define separator alignment between list cells, and configure swipe actions for each cell’s leading and trailing edges. You create an individual list section using [`list(using:layoutEnvironment:)`](nscollectionlayoutsection/list(using:layoutenvironment:).md), or a full list layout using [`list(using:)`](uicollectionviewcompositionallayout/list(using:).md).

You can use a list cell’s [`defaultContentConfiguration()`](uicollectionviewlistcell/defaultcontentconfiguration().md) (Swift)  or [`defaultContentConfiguration`](uicollectionviewlistcell/defaultcontentconfiguration.md) (Objective-C) to get a list content configuration that has preconfigured default styling. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the cell as the current content configuration. For customization options, see [`UIListContentConfiguration`](uilistcontentconfiguration-swift.struct.md).

Alternatively, you can set your content through your own custom subviews using the cell’s [`contentView`](uicollectionviewcell/contentview.md).

## Topics

### Getting a configuration
- [func defaultContentConfiguration() -> UIListContentConfiguration](uicollectionviewlistcell/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the cell’s style.
### Managing cell accessories
- [var accessories: [UICellAccessory]](uicollectionviewlistcell/accessories-8nui4.md)
  An array of the accessories that decorate the cell.
- [struct UICellAccessory](uicellaccessory-swift.struct.md)
  An accessory in a collection view list cell.
### Customizing layout
- [var indentationLevel: Int](uicollectionviewlistcell/indentationlevel.md)
  The level of indentation for the cell.
- [var indentationWidth: CGFloat](uicollectionviewlistcell/indentationwidth.md)
  The width of an indentation level.
- [var indentsAccessories: Bool](uicollectionviewlistcell/indentsaccessories.md)
  A Boolean value that detemines whether the cell indents accessories on the leading side.
- [var separatorLayoutGuide: UILayoutGuide](uicollectionviewlistcell/separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.

## Relationships

### Inherits From
- [UICollectionViewCell](uicollectionviewcell.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UICollectionViewCell](uicollectionviewcell.md)
  A single data item when that item is within the collection view’s visible bounds.
- [class UICollectionReusableView](uicollectionreusableview.md)
  A view that defines the behavior for all cells and supplementary views presented by a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell)*