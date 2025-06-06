# UIActionSheet

**Framework**: UIKit  
**Kind**: class

A view that presents a set of alternatives for how to proceed with a task.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIActionSheet
```

#### Overview

In apps that target versions of iOS prior to iOS 8, use the [`UIActionSheet`](uiactionsheet.md) class to present the user with a set of alternatives for how to proceed with a given task. You can also use action sheets to prompt the user to confirm a potentially dangerous action. The action sheet contains an optional title and one or more buttons, each of which corresponds to an action to take.

Use the properties and methods of this class to configure the action sheet’s message, style, and buttons before presenting it. You should also assign a delegate to your action sheet. Your delegate object is responsible for performing the action associated with any buttons when they’re tapped and should conform to the [`UIActionSheetDelegate`](uiactionsheetdelegate.md) protocol. For more information about implementing the methods of the delegate, see [`UIActionSheetDelegate`](uiactionsheetdelegate.md).

You can present an action sheet from a toolbar, tab bar, button bar item, or from a view. This class takes the starting view and current platform into account when determining how to present the action sheet. For applications running on iPhone and iPod touch devices, the action sheet typically slides up from the bottom of the window that owns the view. For applications running on iPad devices, the action sheet is typically displayed in a popover that’s anchored to the starting view in an appropriate way. Taps outside of the popover automatically dismiss the action sheet, as do taps within any custom buttons. You can also dismiss it programmatically.

When presenting an action sheet on an iPad, there are times when you shouldn’t include a cancel button. If you’re presenting just the action sheet, the system displays the action sheet inside a popover without using an animation. Because taps outside the popover dismiss the action sheet without selecting an item, this results in a default way to cancel the sheet. Including a cancel button would therefore only cause confusion. However, if you have an existing popover and are displaying an action sheet on top of other content using an animation, a cancel button is still appropriate. For more information, see [`iOS Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/).

> ❗ **Important**:  In iOS 4 and later, action sheets aren’t dismissed automatically when an application moves to the background. This behavior differs from earlier versions of the operating system, where action sheets were automatically canceled (and their cancellation handler executed) as part of the termination sequence for the application. Now, it’s up to you to decide whether to dismiss the action sheet (and execute its cancellation handler) or leave it visible for when your application moves back to the foreground. Remember that your application can still be terminated while in the background, so some type of action may be necessary in either case.

 In iOS 4 and later, action sheets aren’t dismissed automatically when an application moves to the background. This behavior differs from earlier versions of the operating system, where action sheets were automatically canceled (and their cancellation handler executed) as part of the termination sequence for the application. Now, it’s up to you to decide whether to dismiss the action sheet (and execute its cancellation handler) or leave it visible for when your application moves back to the foreground. Remember that your application can still be terminated while in the background, so some type of action may be necessary in either case.

##### Subclassing Notes

[`UIActionSheet`](uiactionsheet.md) isn’t designed to be subclassed, nor should you add views to its hierarchy. If you need to present a sheet with more customization than provided by the [`UIActionSheet`](uiactionsheet.md) API, you can create your own and present it modally with [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md).

## Topics

### Creating action sheets
- [convenience init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?, otherButtonTitles: String, String...)](uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:otherbuttontitles:_:).md)
  Creates an action sheet with the specified values.
- [init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?)](uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:).md)
  Initializes the action sheet using the specified starting parameters.
### Setting properties
- [var delegate: (any UIActionSheetDelegate)?](uiactionsheet/delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var title: String](uiactionsheet/title.md)
  The string that appears in the receiver’s title bar.
- [var isVisible: Bool](uiactionsheet/isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.
- [var actionSheetStyle: UIActionSheetStyle](uiactionsheet/actionsheetstyle.md)
  The receiver’s presentation style.
### Configuring buttons
- [func addButton(withTitle: String?) -> Int](uiactionsheet/addbutton(withtitle:).md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](uiactionsheet/numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](uiactionsheet/buttontitle(at:).md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](uiactionsheet/cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](uiactionsheet/destructivebuttonindex.md)
  The index number of the destructive button.
- [var firstOtherButtonIndex: Int](uiactionsheet/firstotherbuttonindex.md)
  The index of the first custom button.
### Presenting the action sheet
- [func show(from: UITabBar)](uiactionsheet/show(from:)-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](uiactionsheet/show(from:)-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(in: UIView)](uiactionsheet/show(in:).md)
  Displays an action sheet that originates from the specified view.
- [func show(from: UIBarButtonItem, animated: Bool)](uiactionsheet/show(from:animated:).md)
  Displays an action sheet that originates from the specified bar button item.
- [func show(from: CGRect, in: UIView, animated: Bool)](uiactionsheet/show(from:in:animated:).md)
  Displays an action sheet that originates from the specified view.
### Dismissing the action sheet
- [func dismiss(withClickedButtonIndex: Int, animated: Bool)](uiactionsheet/dismiss(withclickedbuttonindex:animated:).md)
  Dismisses the action sheet immediately using an optional animation.
### Constants
- [enum UIActionSheetStyle](uiactionsheetstyle.md)
  Specifies the style of an action sheet.

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

- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
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
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIUserNotificationSettings](uiusernotificationsettings.md)
  The types of notifications that can be displayed to the user by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet)*