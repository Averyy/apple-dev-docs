# UIListContentView

**Framework**: UIKit  
**Kind**: class

A content view for displaying list-based content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIListContentView
```

#### Overview

You use a list content view for displaying list-based content in a custom view hierarchy. You can embed a list content view manually in a custom cell or in a container view, like a [`UIStackView`](uistackview.md). You can use Auto Layout or manual layout techniques to size and position the view, and its height adjusts dynamically according to its width and the space it needs to display its content.

A list content view relies on its list content configuration to supply its styling and content. You create a list content view by passing in a [`UIListContentConfiguration`](uilistcontentconfiguration-swift.struct.md) to [`init(configuration:)`](uilistcontentview/init(configuration:).md) (Swift) or [`initWithConfiguration:`](uilistcontentview/initwithconfiguration:.md) (Objective-C). To update the content view, you set a new configuration on it through its [`configuration`](uilistcontentview/configuration.md) property.

If you’re using a [`UICollectionView`](uicollectionview.md) or [`UITableView`](uitableview.md), you don’t need to manually create a list content view to take advantage of the list configuration. Instead, you assign a [`UIListContentConfiguration`](uilistcontentconfiguration-swift.struct.md) to the [`contentConfiguration`](uicollectionviewcell/contentconfiguration-1lcqh.md) property of the cells, headers, or footers within those types.

## Topics

### Creating a list content view
- [convenience init(configuration: UIListContentConfiguration)](uilistcontentview/init(configuration:).md)
  Creates a list content view with the specified content configuration.
- [init?(coder: NSCoder)](uilistcontentview/init(coder:).md)
  Creates a list content view from data in an unarchiver.
### Managing the content layout
- [var textLayoutGuide: UILayoutGuide?](uilistcontentview/textlayoutguide.md)
  A guide for positioning the primary text in the content view.
- [var secondaryTextLayoutGuide: UILayoutGuide?](uilistcontentview/secondarytextlayoutguide.md)
  A guide for positioning the secondary text in the content view.
- [var imageLayoutGuide: UILayoutGuide?](uilistcontentview/imagelayoutguide.md)
  A guide for positioning the image in the content view.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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
- [UIContentView](uicontentview-5fh3z.md)
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

- [struct UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md)
  A content configuration for a list-based content view.
- [protocol UIContentConfiguration](uicontentconfiguration-9eib5.md)
  The requirements for an object that provides the configuration for a content view.
- [protocol UIContentView](uicontentview-5fh3z.md)
  The requirements for a content view that you create using a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentview)*