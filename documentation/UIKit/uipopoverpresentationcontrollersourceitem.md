# UIPopoverPresentationControllerSourceItem

**Framework**: UIKit  
**Kind**: protocol

A type that can be an anchor for a popover presentation controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol UIPopoverPresentationControllerSourceItem : NSObjectProtocol
```

## Topics

### Instance Methods
- [func frame(in: UIView) -> CGRect?](uipopoverpresentationcontrollersourceitem/frame(in:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSUIViewToolbarItem](nsuiviewtoolbaritem.md)
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
- [UIBarButtonItem](uibarbuttonitem.md)
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
- [UIFocusGuide](uifocusguide.md)
- [UIImageView](uiimageview.md)
- [UIInputView](uiinputview.md)
- [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)
- [UILabel](uilabel.md)
- [UILayoutGuide](uilayoutguide.md)
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
- [UISearchTab](uisearchtab.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISlider](uislider.md)
- [UIStackView](uistackview.md)
- [UIStandardTextCursorView](uistandardtextcursorview.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITab](uitab.md)
- [UITabBar](uitabbar.md)
- [UITabBarItem](uitabbaritem.md)
- [UITabGroup](uitabgroup.md)
- [UITableView](uitableview.md)
- [UITableViewCell](uitableviewcell.md)
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)
- [UIToolbar](uitoolbar.md)
- [UITrackingLayoutGuide](uitrackinglayoutguide.md)
- [UIView](uiview.md)
- [UIVisualEffectView](uivisualeffectview.md)
- [UIWebView](uiwebview.md)
- [UIWindow](uiwindow.md)

## See Also

- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](uipopoverpresentationcontroller/sourceitem.md)
  The item on which to anchor the popover.
- [var sourceView: UIView?](uipopoverpresentationcontroller/sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var sourceRect: CGRect](uipopoverpresentationcontroller/sourcerect.md)
  The area in the source view in which you anchor the popover.
- [var barButtonItem: UIBarButtonItem?](uipopoverpresentationcontroller/barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollersourceitem)*