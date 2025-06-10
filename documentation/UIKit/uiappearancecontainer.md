# UIAppearanceContainer

**Framework**: UIKit  
**Kind**: protocol

A protocol that a class must adopt to allow appearance customization using the [`UIAppearance`](uiappearance.md) API.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIAppearanceContainer : NSObjectProtocol
```

#### Overview

To participate in the appearance proxy API, tag appearance property accessor methods in your header with [`UI_APPEARANCE_SELECTOR`](ui_appearance_selector.md).

Appearance property accessor methods must be of the form:

You may have no axes or as many as you like for any property.

The property type may be any standard iOS type: `id`, [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger), [`NSUInteger`](https://developer.apple.com/documentation/ObjectiveC/NSUInteger), [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct), [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint), [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize), [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect), [`UIEdgeInsets`](uiedgeinsets.md) or [`UIOffset`](uioffset.md). Axis parameter values must be either [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) or [`NSUInteger`](https://developer.apple.com/documentation/ObjectiveC/NSUInteger). UIKit throws an exception if other types are used in the axes.

For example, [`UIBarButtonItem`](uibarbuttonitem.md) defines these methods:

- [`setTitlePositionAdjustment(_:for:)`](uibarbuttonitem/settitlepositionadjustment(_:for:).md)
- [`backButtonBackgroundImage(for:barMetrics:)`](uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:).md)
- [`setBackButtonBackgroundImage(_:for:barMetrics:)`](uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
- [UIButton](uibutton.md)
- [UICalendarView](uicalendarview.md)
- [UICloudSharingController](uicloudsharingcontroller.md)
- [UICollectionReusableView](uicollectionreusableview.md)
- [UICollectionView](uicollectionview.md)
- [UICollectionViewCell](uicollectionviewcell.md)
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UICollectionViewListCell](uicollectionviewlistcell.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIColorWell](uicolorwell.md)
- [UIContentUnavailableView](uicontentunavailableview.md)
- [UIControl](uicontrol.md)
- [UIDatePicker](uidatepicker.md)
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](uidocumentviewcontroller.md)
- [UIEventAttributionView](uieventattributionview.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIImageView](uiimageview.md)
- [UIInputView](uiinputview.md)
- [UIInputViewController](uiinputviewcontroller.md)
- [UILabel](uilabel.md)
- [UIListContentView](uilistcontentview.md)
- [UINavigationBar](uinavigationbar.md)
- [UINavigationController](uinavigationcontroller.md)
- [UIPageControl](uipagecontrol.md)
- [UIPageViewController](uipageviewcontroller.md)
- [UIPasteControl](uipastecontrol.md)
- [UIPickerView](uipickerview.md)
- [UIPopoverBackgroundView](uipopoverbackgroundview.md)
- [UIPopoverController](uipopovercontroller.md)
- [UIPopoverPresentationController](uipopoverpresentationcontroller.md)
- [UIPresentationController](uipresentationcontroller.md)
- [UIProgressView](uiprogressview.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UIScrollView](uiscrollview.md)
- [UISearchBar](uisearchbar.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISheetPresentationController](uisheetpresentationcontroller.md)
- [UISlider](uislider.md)
- [UISplitViewController](uisplitviewcontroller.md)
- [UIStackView](uistackview.md)
- [UIStandardTextCursorView](uistandardtextcursorview.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITabBar](uitabbar.md)
- [UITabBarController](uitabbarcontroller.md)
- [UITableView](uitableview.md)
- [UITableViewCell](uitableviewcell.md)
- [UITableViewController](uitableviewcontroller.md)
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
- [UITextField](uitextfield.md)
- [UITextFormattingViewController](uitextformattingviewcontroller.md)
- [UITextView](uitextview.md)
- [UIToolbar](uitoolbar.md)
- [UIVideoEditorController](uivideoeditorcontroller.md)
- [UIView](uiview.md)
- [UIViewController](uiviewcontroller.md)
- [UIVisualEffectView](uivisualeffectview.md)
- [UIWebView](uiwebview.md)
- [UIWindow](uiwindow.md)

## See Also

- [protocol UIAppearance](uiappearance.md)
  A collection of methods that gives you access to the appearance proxy for a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearancecontainer)*