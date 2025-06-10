# UICollectionViewCell

**Framework**: UIKit  
**Kind**: class

A single data item when that item is within the collection view’s visible bounds.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewCell
```

#### Overview

You can use [`UICollectionViewCell`](uicollectionviewcell.md) as-is or subclass it to add additional properties and methods. The layout and presentation of cells is managed by the collection view and its corresponding layout object.

To configure the content and appearance of your cell, you can set its [`contentConfiguration`](uicollectionviewcell/contentconfiguration-13e7k.md) and [`backgroundConfiguration`](uicollectionviewcell/backgroundconfiguration-rgj4.md). Alternatively, add the views needed to present the data item’s content as subviews to the view in the [`contentView`](uicollectionviewcell/contentview.md) property. Don’t directly add subviews to the cell itself. The cell manages multiple layers of content, of which the content view is only one. In addition to the content view, the cell manages two background views that display the cell in its selected and unselected states.

You typically don’t create instances of this class yourself. Instead, you register your specific cell subclass (or a nib file containing a configured instance of your class) using a cell registration. When you want a new instance of your cell class, call the [`dequeueConfiguredReusableCell(using:for:item:)`](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md) (Swift) or [`dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:`](uicollectionview/dequeueconfiguredreusablecellwithregistration:forindexpath:item:.md) (Objective-C) method of the collection view object to retrieve one.

## Topics

### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uicollectionviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uicollectionviewcell/backgroundconfiguration-rgj4.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uicollectionviewcell/backgroundview.md)
  The view that displays behind the cell’s other content.
- [var selectedBackgroundView: UIView?](uicollectionviewcell/selectedbackgroundview.md)
  The view that displays just above the background view for a selected cell.
### Managing the content
- [var contentConfiguration: (any UIContentConfiguration)?](uicollectionviewcell/contentconfiguration-13e7k.md)
  The current content configuration of the cell.
- [var automaticallyUpdatesContentConfiguration: Bool](uicollectionviewcell/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [var contentView: UIView](uicollectionviewcell/contentview.md)
  The main view that you add your cell’s custom content to.
### Managing the state
- [var configurationState: UICellConfigurationState](uicollectionviewcell/configurationstate-4u37h.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](uicollectionviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCell.ConfigurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](uicollectionviewcell/isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](uicollectionviewcell/ishighlighted.md)
  The highlight state of the cell.
### Managing drag state changes
- [func dragStateDidChange(UICollectionViewCell.DragState)](uicollectionviewcell/dragstatedidchange(_:).md)
  Called when the drag state of the cell changes.
- [UICollectionViewCell.DragState](uicollectionviewcell/dragstate.md)
  Constants indicating the current state of the drag operation.

## Relationships

### Inherits From
- [UICollectionReusableView](uicollectionreusableview.md)
### Inherited By
- [UICollectionViewListCell](uicollectionviewlistcell.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [class UICollectionViewListCell](uicollectionviewlistcell.md)
  A collection view cell that provides list features and default styling.
- [class UICollectionReusableView](uicollectionreusableview.md)
  A view that defines the behavior for all cells and supplementary views presented by a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell)*