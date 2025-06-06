# UIRefreshControl

**Framework**: UIKit  
**Kind**: class

A standard control that can initiate the refreshing of a scroll view’s contents.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIRefreshControl
```

## Mentions

- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)

#### Overview

A [`UIRefreshControl`](uirefreshcontrol.md) object is a standard control that you attach to any [`UIScrollView`](uiscrollview.md) object, including table views and collection views. Add this control to scrollable views to give your users a standard way to refresh their contents. When the user drags the top of the scrollable content area downward, the scroll view reveals the refresh control, begins animating its progress indicator, and notifies your app. You use that notification to update your content and dismiss the refresh control.

![Illustration showing a refresh control. The control displays an animated progress indicator at the top of a scroll view’s content area.](https://docs-assets.developer.apple.com/published/f81e2b2c339c5ed3da70cdd7b768331e/media-3148903%402x.png)

The refresh control lets you know when to update your content using the target-action mechanism of [`UIControl`](uicontrol.md). Upon activation, the refresh control calls the action method you provided at configuration time. When adding your action method, configure it to listen for the [`valueChanged`](uicontrol/event/valuechanged.md) event, as shown in the following example code. Use your action method to update your content, and call the refresh control’s [`endRefreshing()`](uirefreshcontrol/endrefreshing().md) method when you’re done.

```swift
func configureRefreshControl () {
   // Add the refresh control to your UIScrollView object.
   myScrollingView.refreshControl = UIRefreshControl()
   myScrollingView.refreshControl?.addTarget(self, action:
                                      #selector(handleRefreshControl),
                                      for: .valueChanged)
}
    
@objc func handleRefreshControl() {
   // Update your content…

   // Dismiss the refresh control.
   DispatchQueue.main.async {
      self.myScrollingView.refreshControl?.endRefreshing()
   }
}

```

If you’re using a [`UITableViewController`](uitableviewcontroller.md), assign its [`refreshControl`](uitableviewcontroller/refreshcontrol.md) property to an instance of [`UIRefreshControl`](uirefreshcontrol.md). Then associate a target and action method for the [`valueChanged`](uicontrol/event/valuechanged.md) event to manage the refresh behavior of the associated table view.

> ❗ **Important**:  [`UIRefreshControl`](uirefreshcontrol.md) isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md). However, you can update your app to provide similar functionality in the Mac idiom. For example, replace the control with a Refresh menu item by creating a [`UIKeyCommand`](uikeycommand.md) object with the title “Refresh” and the keyboard shortcut Command-R. Then add the command to your app’s menu system. For more information, see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

 [`UIRefreshControl`](uirefreshcontrol.md) isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md). However, you can update your app to provide similar functionality in the Mac idiom. For example, replace the control with a Refresh menu item by creating a [`UIKeyCommand`](uikeycommand.md) object with the title “Refresh” and the keyboard shortcut Command-R. Then add the command to your app’s menu system. For more information, see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Topics

### Initializing a refresh control
- [init()](uirefreshcontrol/init.md)
  Initializes and returns a standard refresh control.
### Accessing the control attributes
- [var tintColor: UIColor!](uirefreshcontrol/tintcolor.md)
  The tint color for the refresh control.
- [var attributedTitle: NSAttributedString?](uirefreshcontrol/attributedtitle.md)
  The styled title text to display in the refresh control.
### Managing the refresh status
- [func beginRefreshing()](uirefreshcontrol/beginrefreshing.md)
  Tells the control that a refresh operation was started programmatically.
- [func endRefreshing()](uirefreshcontrol/endrefreshing.md)
  Tells the control that a refresh operation has ended.
- [var isRefreshing: Bool](uirefreshcontrol/isrefreshing.md)
  A Boolean value indicating whether a refresh operation has been triggered and is in progress.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
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
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
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

- [var indicatorStyle: UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.property.md)
  The style of the scroll indicators.
- [UIScrollView.IndicatorStyle](uiscrollview/indicatorstyle-swift.enum.md)
  Defines constants that represent the styles of the scroll indicators.
- [var showsHorizontalScrollIndicator: Bool](uiscrollview/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](uiscrollview/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var horizontalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/horizontalscrollindicatorinsets.md)
  The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [var verticalScrollIndicatorInsets: UIEdgeInsets](uiscrollview/verticalscrollindicatorinsets.md)
  The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [var automaticallyAdjustsScrollIndicatorInsets: Bool](uiscrollview/automaticallyadjustsscrollindicatorinsets.md)
  A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [func flashScrollIndicators()](uiscrollview/flashscrollindicators.md)
  Displays the scroll indicators momentarily.
- [func withScrollIndicatorsShown(forContentOffsetChanges: () -> Void)](uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:).md)
  Displays the scroll indicators during updates to the scroll view’s content offset.
- [var refreshControl: UIRefreshControl?](uiscrollview/refreshcontrol.md)
  The refresh control associated with the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirefreshcontrol)*