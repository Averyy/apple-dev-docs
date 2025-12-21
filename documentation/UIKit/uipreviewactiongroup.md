# UIPreviewActionGroup

**Framework**: UIKit  
**Kind**: class

A group of one or more child quick actions, each an instance of the preview action class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
class UIPreviewActionGroup
```

#### Overview

When first displayed, the group appears as a single option in a peek quick action sheet. If the user selects the group, a submenu opens, displaying the child quick actions.

## Topics

### Creating a peek quick action group
- [convenience init(title: String, style: UIPreviewAction.Style, actions: [UIPreviewAction])](uipreviewactiongroup/init(title:style:actions:).md)
  Creates a peek quick action group using a specified title, style, and array of peek quick actions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIPreviewActionItem](uipreviewactionitem.md)

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
- [class UIMutableUserNotificationAction](uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](uipreviewaction.md)
  A preview action, or , that displays below a peek when a user swipes the peek upward.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewactiongroup)*