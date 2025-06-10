# UILargeContentViewerItem

**Framework**: UIKit  
**Kind**: protocol

Methods that provide details about how to display your custom content in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UILargeContentViewerItem : NSObjectProtocol
```

## Topics

### Integrating with the large content viewer
- [var showsLargeContentViewer: Bool](uilargecontentvieweritem/showslargecontentviewer.md)
  A Boolean value that indicates whether or not to show the item in the large content viewer.
### Configuring display properties
- [var largeContentTitle: String?](uilargecontentvieweritem/largecontenttitle.md)
  A string that describes an item to display in the large content viewer.
- [var largeContentImage: UIImage?](uilargecontentvieweritem/largecontentimage.md)
  An image that represents an item to display in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uilargecontentvieweritem/largecontentimageinsets.md)
  Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
- [var scalesLargeContentImage: Bool](uilargecontentvieweritem/scaleslargecontentimage.md)
  A Boolean value that indicates whether the view scales the item’s image to a larger size or not.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
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

- [class UILargeContentViewerInteraction](uilargecontentviewerinteraction.md)
  An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.
- [protocol UILargeContentViewerInteractionDelegate](uilargecontentviewerinteractiondelegate.md)
  An object that customizes the behavior of the large content viewer interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentvieweritem)*