# SWAttributionView

**Framework**: Shared With You  
**Kind**: class

A view that displays the sender who shares a highlight and provides related actions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class SWAttributionView
```

## Mentions

- [Making your app content shareable](making-your-app-content-shareable.md)

#### Overview

The `SWAttributionView` also allows users to get back to the conversation about the [`SWHighlight`](swhighlight.md) content, and other related actions using a [`highlightMenu`](swattributionview/highlightmenu.md).

Place an `SWAttributionView` next to the content represented by its `SWHighlight`. The `SWAttributionView` displays the names and avatars within the provided horizontal space.

You can constrain this view’s width anchor or set its frame width to control the maximum width of its contents after which truncation may occur. Don’t constrain the view’s height, as the height is dependent on the [`preferredContentSizeCategory`](https://developer.apple.com/documentation/UIKit/UIApplication/preferredContentSizeCategory), and the resulting font size. To provide enough vertical space around this view, reference its [`heightAnchor`](https://developer.apple.com/documentation/UIKit/UIView/heightAnchor) when using Auto Layout, or its [`intrinsicContentSize`](https://developer.apple.com/documentation/UIKit/UIView/intrinsicContentSize) when using manual layout.

## Topics

### Customizing highlights
- [var backgroundStyle: SWAttributionView.BackgroundStyle](swattributionview/backgroundstyle-swift.property.md)
  The background style of the child view that contains names and avatars.
- [var displayContext: SWAttributionView.DisplayContext](swattributionview/displaycontext-swift.property.md)
  The context for the content the system displays with this view.
- [var highlight: SWHighlight?](swattributionview/highlight.md)
  The highlight you use to display this attribution.
- [var highlightMenu: UIMenu](swattributionview/highlightmenu.md)
  A menu with a list of system actions specific to this hightlight.
- [var horizontalAlignment: SWAttributionView.HorizontalAlignment](swattributionview/horizontalalignment-swift.property.md)
  The horizontal alignment of the view.
- [var menuTitleForHideAction: String?](swattributionview/menutitleforhideaction.md)
  A localized string the system uses as a custom title for the hide menu item.
- [var preferredMaxLayoutWidth: CGFloat](swattributionview/preferredmaxlayoutwidth.md)
  A width the system uses to constrain the view contents.
- [var supplementalMenu: UIMenu?](swattributionview/supplementalmenu.md)
  A supplemental menu to augment the attribution view’s existing menu.
### Customizing the view
- [SWAttributionView.BackgroundStyle](swattributionview/backgroundstyle-swift.enum.md)
  The background styling of the attribution view’s contents.
- [SWAttributionView.DisplayContext](swattributionview/displaycontext-swift.enum.md)
  The context for the content that influences the ranking of this view’s highlight.
- [SWAttributionView.HorizontalAlignment](swattributionview/horizontalalignment-swift.enum.md)
  The horizontal alignment of attribution view’s contents.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview)*