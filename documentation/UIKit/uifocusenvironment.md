# UIFocusEnvironment

**Framework**: UIKit  
**Kind**: protocol

A set of methods that define the focus behavior for a branch of the view hierarchy.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFocusEnvironment : NSObjectProtocol
```

#### Overview

The [`UIFocusEnvironment`](uifocusenvironment.md) protocol provides a common interface for specifying and reacting to focus behavior throughout your app. Classes in UIKit that conform to this protocol include [`UIView`](uiview.md), [`UIViewController`](uiviewcontroller.md), [`UIWindow`](uiwindow.md), and [`UIPresentationController`](uipresentationcontroller.md) — in other words, classes that are either directly or indirectly in control of views on the screen.

## Topics

### Requesting focus update
- [func setNeedsFocusUpdate()](uifocusenvironment/setneedsfocusupdate.md)
  Submits a request to the focus engine for a focus update in this environment.
- [func updateFocusIfNeeded()](uifocusenvironment/updatefocusifneeded.md)
  Tells the focus engine to force a focus update immediately.
### Validating focus movements
- [func shouldUpdateFocus(in: UIFocusUpdateContext) -> Bool](uifocusenvironment/shouldupdatefocus(in:).md)
  Returns a Boolean value indicating whether the focus engine should allow the focus update described by the specified context to occur.
### Responding to focus updates
- [func didUpdateFocus(in: UIFocusUpdateContext, with: UIFocusAnimationCoordinator)](uifocusenvironment/didupdatefocus(in:with:).md)
  Called immediately after the system updates the focus to a new view.
### Controlling user-generated focus movements
- [var preferredFocusEnvironments: [any UIFocusEnvironment]](uifocusenvironment/preferredfocusenvironments.md)
  An array of focus environments, ordered by priority, to which this environment prefers focus to be directed during a focus update.
- [var preferredFocusedView: UIView?](uifocusenvironment/preferredfocusedview.md)
  Specifies the view that should be focused if this environment is focused.
### Getting the sound to play during updates
- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)
  Customize the sounds users hear when focus moves.
- [func soundIdentifierForFocusUpdate(in: UIFocusUpdateContext) -> UIFocusSoundIdentifier?](uifocusenvironment/soundidentifierforfocusupdate(in:).md)
  Asks the delegate for the identifier of the sound to play when the object gains focus.
- [struct UIFocusSoundIdentifier](uifocussoundidentifier.md)
  An identifier for a focus-related sound.
### Checking the ancestry of the environment
- [func contains(any UIFocusEnvironment) -> Bool](uifocusenvironment/contains(_:).md)
  Returns a Boolean value that indicates whether the focus environment contains the specified environment.
- [var parentFocusEnvironment: (any UIFocusEnvironment)?](uifocusenvironment/parentfocusenvironment.md)
  The parent focus environment for this environment.
- [var focusItemContainer: (any UIFocusItemContainer)?](uifocusenvironment/focusitemcontainer.md)
  The container for the child focus items in this focus environment.
### Identifying the focus group
- [var focusGroupIdentifier: String?](uifocusenvironment/focusgroupidentifier.md)
  The identifier of the focus group that the environment belongs to.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIFocusItem](uifocusitem.md)
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

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md)
  Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)
  Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [class UIFocusSystem](uifocussystem.md)
  Queries and reevaluates the currently focused item.
- [class UIFocusUpdateContext](uifocusupdatecontext.md)
  An object that provides information relevant to a specific focus update from one view to another.
- [protocol UIFocusItem](uifocusitem.md)
  An object that can become focused.
- [class UIFocusMovementHint](uifocusmovementhint.md)
  Provides movement hint information for the focused item.
- [protocol UIFocusItemContainer](uifocusitemcontainer.md)
  The container responsible for providing geometric context to focus items within a given focus environment.
- [protocol UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
  A type of focus item container that supports automatic scrolling of focusable content.
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment)*