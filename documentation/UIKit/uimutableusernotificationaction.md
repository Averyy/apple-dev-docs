# UIMutableUserNotificationAction

**Framework**: UIKit  
**Kind**: class

A modifiable version of the user notification action class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIMutableUserNotificationAction
```

#### Overview

When a notification is delivered, the system displays a button for each custom action associated with the notification. Tapping a button launches your app (either in the foreground or background) and gives you a chance to perform the indicated action. You use this class to configure the details about the button that is displayed and the information your app needs to perform the corresponding action.

To associate custom actions with a local or remote notification, create one or more instances of this class and use them to configure one or more UIMutableUserNotificationActionSettings objects. An action settings objects defines the set of actions to associate with a single notification. You register your app’s action settings objects at launch time, along with your app’s preferred notification options, using a [`UIUserNotificationSettings`](uiusernotificationsettings.md) object.

For each action you define, you must specify whether execution of that action requires the app to be running in the foreground or background. You can also specify whether the device must be unlocked or can remain locked while the action is performed. Unlocking the device may be necessary if the action involves reading or writing files that are encrypted on disk using the system’s data protection mechanism. When the user selects an action, the system puts your app into the appropriate mode and calls your app delegate’s [`application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:).md) or [`application(_:handleActionWithIdentifier:for:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md) method to perform the action.

## Topics

### Getting the action information
- [var identifier: String?](uimutableusernotificationaction/identifier.md)
  The string that you use internally to identify the action.
- [var title: String?](uimutableusernotificationaction/title.md)
  The localized string to use as the button title for the action.
### Configuring the action’s behavior
- [var activationMode: UIUserNotificationActivationMode](uimutableusernotificationaction/activationmode.md)
  The mode in which to run the app when the action is performed.
- [var isAuthenticationRequired: Bool](uimutableusernotificationaction/isauthenticationrequired.md)
  A Boolean value indicating whether the user must unlock the device before the action is performed.
- [var isDestructive: Bool](uimutableusernotificationaction/isdestructive.md)
  A Boolean value indicating whether the action is destructive.
- [var behavior: UIUserNotificationActionBehavior](uimutableusernotificationaction/behavior.md)
  The custom behavior (if any) that the action supports.
- [var parameters: [AnyHashable : Any]](uimutableusernotificationaction/parameters.md)
  A dictionary of additional parameters to include with the action.

## Relationships

### Inherits From
- [UIUserNotificationAction](uiusernotificationaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction)*