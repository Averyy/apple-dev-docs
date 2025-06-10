# UIPasteConfigurationSupporting

**Framework**: UIKit  
**Kind**: protocol

The interface that determines whether a responder object supports paste configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIPasteConfigurationSupporting : NSObjectProtocol
```

## Topics

### Accessing the paste configuration
- [var pasteConfiguration: UIPasteConfiguration?](uipasteconfigurationsupporting/pasteconfiguration.md)
  The paste configuration associated with the responder object.
### Performing a paste operation
- [func canPaste([NSItemProvider]) -> Bool](uipasteconfigurationsupporting/canpaste(_:).md)
  Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.
- [func paste(itemProviders: [NSItemProvider])](uipasteconfigurationsupporting/paste(itemproviders:).md)
  Performs a paste operation on the responder object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UITextDroppable](uitextdroppable.md)
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
### Conforming Types
- [UIAccessibilityElement](uiaccessibilityelement.md)
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UIAlertView](uialertview.md)
- [UIApplication](uiapplication.md)
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
- [UIProgressView](uiprogressview.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UIResponder](uiresponder.md)
- [UIScene](uiscene.md)
- [UIScrollView](uiscrollview.md)
- [UISearchBar](uisearchbar.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
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
- [UIWindowScene](uiwindowscene.md)

## See Also

- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting)*