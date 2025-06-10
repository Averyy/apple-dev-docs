# UIAppearance

**Framework**: UIKit  
**Kind**: protocol

A collection of methods that gives you access to the appearance proxy for a class.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIAppearance : NSObjectProtocol
```

#### Overview

You can customize the appearance of instances of a class by sending appearance-modification messages to the class’s appearance proxy.

> **Note**:  iOS applies appearance changes when a view enters a window, but it doesn’t change the appearance of a view that’s already in a window. To change the appearance of a view that’s currently in a window, remove the view from the view hierarchy and then put it back.

There are two ways to customize appearance for objects: for all instances, and for instances contained within an instance of a container class.

To customize the appearance of all instances of a class, use [`appearance()`](uiappearance/appearance().md) to get the appearance proxy for the class. For example, to modify the bar background tint color for all instances of [`UINavigationBar`](uinavigationbar.md):

```swift
UINavigationBar.appearance().barTintColor = navBarTintColor
```

To customize the appearances for instances of a class when contained within an instance of a container class, or instances in a hierarchy, use [`appearanceWhenContainedIn:`](uiappearance/appearancewhencontainedin:.md) to get the appearance proxy for the class. For example, to modify the appearance of bar buttons, based on the object that contains the navigation bar:

```swift
let navigationBarAppearance =
UINavigationBar.appearance(whenContainedInInstancesOf: [UINavigationController.self])
navigationBarAppearance.setBackgroundImage(navBarBackgroundImage, for: .any, barMetrics: .default)

let barButtonNavigationBarAppearance =
UIBarButtonItem.appearance(whenContainedInInstancesOf: [UINavigationBar.self])
barButtonNavigationBarAppearance.setBackgroundImage(barButtonNavBarImage, for: .normal, barMetrics: .default)

let barButtonToolbarAppearance =
UIBarButtonItem.appearance(whenContainedInInstancesOf: [UIToolbar.self])
barButtonToolbarAppearance.setBackgroundImage(barButtonToolbarImage, for: .normal, barMetrics: .default)
```

In any given view hierarchy, the outermost appearance proxy wins. Specificity (depth of the chain) is the tie-breaker. In other words, the containment statement in [`appearanceWhenContainedIn:`](uiappearance/appearancewhencontainedin:.md) is treated as a partial ordering. Given a concrete ordering (actual subview hierarchy), UIKit selects the partial ordering that’s the first unique match when reading the actual hierarchy from the window down.

You can further refine which instances of a class will have their appearance customized by specifying a trait collection. Use the [`appearance(for:)`](uiappearance/appearance(for:).md) and [`appearanceForTraitCollection:whenContainedIn:`](uiappearance/appearancefortraitcollection:whencontainedin:.md) methods to retrieve the proxy for a class with the specified trait collection.

To support appearance customization, a class must conform to the [`UIAppearanceContainer`](uiappearancecontainer.md) protocol and relevant accessor methods must be marked with [`UI_APPEARANCE_SELECTOR`](ui_appearance_selector.md).

## Topics

### Working with the appearance proxy
- [static func appearance() -> Self](uiappearance/appearance.md)
  Returns the appearance proxy for the receiver.
- [static func appearance(for: UITraitCollection) -> Self](uiappearance/appearance(for:).md)
  Returns the appearance proxy for the receiver that has the passed trait collection.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(for:whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
- [UIBarButtonItem](uibarbuttonitem.md)
- [UIBarItem](uibaritem.md)
- [UIButton](uibutton.md)
- [UICalendarView](uicalendarview.md)
- [UICollectionReusableView](uicollectionreusableview.md)
- [UICollectionView](uicollectionview.md)
- [UICollectionViewCell](uicollectionviewcell.md)
- [UICollectionViewListCell](uicollectionviewlistcell.md)
- [UIColorWell](uicolorwell.md)
- [UIContentUnavailableView](uicontentunavailableview.md)
- [UIControl](uicontrol.md)
- [UIDatePicker](uidatepicker.md)
- [UIEventAttributionView](uieventattributionview.md)
- [UIImageView](uiimageview.md)
- [UIInputView](uiinputview.md)
- [UILabel](uilabel.md)
- [UIListContentView](uilistcontentview.md)
- [UINavigationBar](uinavigationbar.md)
- [UIPageControl](uipagecontrol.md)
- [UIPasteControl](uipastecontrol.md)
- [UIPickerView](uipickerview.md)
- [UIPopoverBackgroundView](uipopoverbackgroundview.md)
- [UIProgressView](uiprogressview.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UIScrollView](uiscrollview.md)
- [UISearchBar](uisearchbar.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISlider](uislider.md)
- [UIStackView](uistackview.md)
- [UIStandardTextCursorView](uistandardtextcursorview.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITabBar](uitabbar.md)
- [UITabBarItem](uitabbaritem.md)
- [UITableView](uitableview.md)
- [UITableViewCell](uitableviewcell.md)
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)
- [UIToolbar](uitoolbar.md)
- [UIView](uiview.md)
- [UIVisualEffectView](uivisualeffectview.md)
- [UIWebView](uiwebview.md)
- [UIWindow](uiwindow.md)

## See Also

- [protocol UIAppearanceContainer](uiappearancecontainer.md)
  A protocol that a class must adopt to allow appearance customization using the [`UIAppearance`](uiappearance.md) API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance)*