# UIAlertView

**Framework**: UIKit  
**Kind**: class

A view that displays an alert message.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIAlertView
```

#### Overview

In apps that run in versions of iOS prior to iOS 8, use the [`UIAlertView`](uialertview.md) class to display an alert message to the user. An alert view functions similar to but differs in appearance from an action sheet (an instance of [`UIActionSheet`](uiactionsheet.md)).

##### Using an Alert View

Use the properties and methods defined in this class to set the title, message, and delegate of an alert view and configure the buttons in apps that run in versions of iOS prior to iOS 8. You must set a delegate if you add custom buttons. The delegate should conform to the [`UIAlertViewDelegate`](uialertviewdelegate.md) protocol. Use the [`show()`](uialertview/show().md) method to display an alert view after it’s configured.

##### Subclassing Notes

The [`UIAlertView`](uialertview.md) class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Topics

### Creating alert views
- [convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)](uialertview/init(title:message:delegate:cancelbuttontitle:).md)
  Convenience method for initializing an alert view.
- [convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles: String, String...)](uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:).md)
  Creates an alert view with the specified values.
- [init(frame: CGRect)](uialertview/init(frame:).md)
  Creates an alert view with the specified frame.
- [init?(coder: NSCoder)](uialertview/init(coder:).md)
  Creates an alert view from data in an unarchiver.
### Setting properties
- [var delegate: AnyObject?](uialertview/delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var alertViewStyle: UIAlertViewStyle](uialertview/alertviewstyle.md)
  The kind of alert displayed to the user.
- [var title: String](uialertview/title.md)
  The string that appears in the receiver’s title bar.
- [var message: String?](uialertview/message.md)
  Descriptive text that provides more details than the title.
- [var isVisible: Bool](uialertview/isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.
### Configuring buttons
- [func addButton(withTitle: String?) -> Int](uialertview/addbutton(withtitle:).md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](uialertview/numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](uialertview/buttontitle(at:).md)
  Returns the title of the button at the given index.
- [func textField(at: Int) -> UITextField?](uialertview/textfield(at:).md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](uialertview/cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](uialertview/firstotherbuttonindex.md)
  The index of the first other button.
### Displaying
- [func show()](uialertview/show.md)
  Displays the receiver using animation.
### Dismissing
- [func dismiss(withClickedButtonIndex: Int, animated: Bool)](uialertview/dismiss(withclickedbuttonindex:animated:).md)
  Dismisses the receiver, optionally with animation.
### Constants
- [enum UIAlertViewStyle](uialertviewstyle.md)
  The presentation style of the alert.

## Relationships

### Inherits From
- [UIView](uiview.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
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

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](uipreviewaction.md)
  A preview action, or , that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UISearchDisplayController](uisearchdisplaycontroller.md)
  An object that manages the display of a search bar, along with a table view that displays search results.
- [class UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview)*