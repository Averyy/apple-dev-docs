# UIMenuController

**Framework**: UIKit  
**Kind**: class

The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMenuController
```

#### Overview

The singleton [`UIMenuController`](uimenucontroller.md) instance is referred to as the editing menu. When you make this menu visible, [`UIMenuController`](uimenucontroller.md) positions it relative to a target rectangle on the screen; this rectangle usually defines a selection. The menu appears above the target rectangle or, if there isn’t enough space for it, below it. The menu’s pointer is placed at the center of the top or bottom of the target rectangle, as appropriate. Be sure to set the tracking rectangle before you make the menu visible. You’re also responsible for detecting, tracking, and displaying selections.

The [`UIResponderStandardEditActions`](uiresponderstandardeditactions.md) informal protocol declares methods that are invoked when the user taps a menu command. The [`canPerformAction(_:withSender:)`](uiresponder/canperformaction(_:withsender:).md) method of [`UIResponder`](uiresponder.md) is also related to the editing menu. A responder implements this method to enable and disable commands of the editing menu just before the menu is displayed. You can force the menu commands enabled state to update by calling the [`update()`](uimenucontroller/update().md) method.

You can also provide your own menu items via the [`menuItems`](uimenucontroller/menuitems.md) property. When you modify the menu items, you can use the [`update()`](uimenucontroller/update().md) method to force the menu to update its display.

## Topics

### Getting the menu controller instance
- [class var shared: UIMenuController](uimenucontroller/shared.md)
  Returns the menu controller.
### Showing and hiding the menu
- [func showMenu(from: UIView, rect: CGRect)](uimenucontroller/showmenu(from:rect:).md)
- [func hideMenu(from: UIView)](uimenucontroller/hidemenu(from:).md)
- [func hideMenu()](uimenucontroller/hidemenu.md)
- [var isMenuVisible: Bool](uimenucontroller/ismenuvisible.md)
  The visibility of the editing menu.
- [func setMenuVisible(Bool, animated: Bool)](uimenucontroller/setmenuvisible(_:animated:).md)
  Shows or hides the editing menu, optionally animating the action.
### Positioning the menu
- [var menuFrame: CGRect](uimenucontroller/menuframe.md)
  Returns the frame of the editing menu.
- [var arrowDirection: UIMenuController.ArrowDirection](uimenucontroller/arrowdirection-swift.property.md)
  The direction the arrow of the editing menu is pointing.
- [UIMenuController.ArrowDirection](uimenucontroller/arrowdirection-swift.enum.md)
  The direction the arrow of the editing menu is pointing.
- [func setTargetRect(CGRect, in: UIView)](uimenucontroller/settargetrect(_:in:).md)
  Sets the area in a view above or below which the editing menu is positioned.
### Updating the menu
- [func update()](uimenucontroller/update.md)
  Updates the appearance and enabled state of menu commands.
### Customizing menu items
- [var menuItems: [UIMenuItem]?](uimenucontroller/menuitems.md)
  The custom menu items for the editing menu.
### Notifications
- [class let willShowMenuNotification: NSNotification.Name](uimenucontroller/willshowmenunotification.md)
  Posted by the menu controller just before it shows the menu.
- [class let didShowMenuNotification: NSNotification.Name](uimenucontroller/didshowmenunotification.md)
  Posted by the menu controller just after it shows the menu.
- [class let willHideMenuNotification: NSNotification.Name](uimenucontroller/willhidemenunotification.md)
  Posted by the menu controller just before it hides the menu.
- [class let didHideMenuNotification: NSNotification.Name](uimenucontroller/didhidemenunotification.md)
  Posted by the menu controller just after it hides the menu.
- [class let menuFrameDidChangeNotification: NSNotification.Name](uimenucontroller/menuframedidchangenotification.md)
  Posted when the frame of a visible menu changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller)*