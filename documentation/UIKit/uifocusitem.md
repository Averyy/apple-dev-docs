# UIFocusItem

**Framework**: UIKit  
**Kind**: protocol

An object that can become focused.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFocusItem : UIFocusEnvironment
```

#### Overview

An object that conforms to the [`UIFocusItem`](uifocusitem.md) protocol is capable of participating in the focus system; further, only [`UIFocusItem`](uifocusitem.md) objects can be focused.

Even when an object that conforms to [`UIFocusItem`](uifocusitem.md) isn’t currently focusable, it may still have an effect on the focus system. For example, items that aren’t focusable, but that completely obscure other items, may prevent those other items from being focusable, because they aren’t visible to the user. Also, because [`UIFocusItem`](uifocusitem.md) conforms to [`UIFocusEnvironment`](uifocusenvironment.md), items that aren’t focusable may still affect the focus behavior of items they contain, or react to focus updates.

## Topics

### Determining focusability
- [var canBecomeFocused: Bool](uifocusitem/canbecomefocused.md)
  A Boolean value that indicates whether the item can become focused.
- [var isFocused: Bool](uifocusitem/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
### Retrieving the item frame
- [var frame: CGRect](uifocusitem/frame.md)
  The geometric frame of the item.
### Determining the focus priority
- [var focusGroupPriority: UIFocusGroupPriority](uifocusitem/focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
### Providing movement hints
- [func didHintFocusMovement(UIFocusMovementHint)](uifocusitem/didhintfocusmovement(_:).md)
  Indicates to the currently focused item that focus movement might occur.
- [class UIFocusMovementHint](uifocusmovementhint.md)
  Provides movement hint information for the focused item.
### Indicating focus visually
- [var focusEffect: UIFocusEffect?](uifocusitem/focuseffect.md)
  The visual effect to apply when the item becomes focused.
### Working with transparent items
- [var isTransparentFocusItem: Bool](uifocusitem/istransparentfocusitem.md)
  Indicates if the focus item is transparent, which allows items behind it to become focused.
### Instance Properties
- [var focusItemDeferralMode: UIFocusItemDeferralMode](uifocusitem/focusitemdeferralmode.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIFocusEnvironment](uifocusenvironment.md)
### Conforming Types
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
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

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md)
  Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)
  Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [protocol UIFocusEnvironment](uifocusenvironment.md)
  A set of methods that define the focus behavior for a branch of the view hierarchy.
- [class UIFocusSystem](uifocussystem.md)
  Queries and reevaluates the currently focused item.
- [class UIFocusUpdateContext](uifocusupdatecontext.md)
  An object that provides information relevant to a specific focus update from one view to another.
- [class UIFocusMovementHint](uifocusmovementhint.md)
  Provides movement hint information for the focused item.
- [protocol UIFocusItemContainer](uifocusitemcontainer.md)
  The container responsible for providing geometric context to focus items within a given focus environment.
- [protocol UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
  A type of focus item container that supports automatic scrolling of focusable content.
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem)*