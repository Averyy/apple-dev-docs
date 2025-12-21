# UILocalNotification

**Framework**: UIKit  
**Kind**: class

A notification that an app can schedule for presentation at a specific date and time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
class UILocalNotification
```

#### Overview

The operating system is responsible for delivering local notifications at their scheduled times; the app does not have to be running for this to happen. Although local notifications are similar to remote notifications in that they are used for displaying alerts, playing sounds, and badging app icons, they are composed and delivered locally and do not require connection with remote servers.

Local notifications are primarily intended for apps with timer-based behaviors and simple calendar or to-do list apps. An app that is running in the background may also schedule a local notification to inform the user of an incoming message, chat, or update. An app can have only a limited number of scheduled notifications; the system keeps the soonest-firing 64 notifications (with automatically rescheduled notifications counting as a single notification) and discards the rest.

When you create a local notification, you must specify either a specific date or a geographic region as the trigger for delivering the notification. Date-based notifications are delivered at the day and time you specify, and allowances can be made for time zone changes as needed. Region-based notifications are delivered when the user enters or exits the specified region. In both cases, you can specify whether the notifications are one-time events or can be rescheduled and delivered again.

After creating a `UILocalNotification` object, schedule it using either the [`scheduleLocalNotification(_:)`](uiapplication/schedulelocalnotification(_:).md) or [`presentLocalNotificationNow(_:)`](uiapplication/presentlocalnotificationnow(_:).md) method of the [`UIApplication`](uiapplication.md) class. The [`scheduleLocalNotification(_:)`](uiapplication/schedulelocalnotification(_:).md) method uses the fire date to schedule delivery; the [`presentLocalNotificationNow(_:)`](uiapplication/presentlocalnotificationnow(_:).md) method presents the notification immediately, regardless of the value of `fireDate`. You can cancel one or more local notifications using the [`cancelLocalNotification(_:)`](uiapplication/cancellocalnotification(_:).md) or [`cancelAllLocalNotifications()`](uiapplication/cancelalllocalnotifications().md) method of the [`UIApplication`](uiapplication.md) object.

When the system delivers a local notification, several things can happen, depending on the app state and the type of notification. If the app is not frontmost and visible, the system displays the alert message, badges the app, and plays a sound—whatever is specified in the notification. If the notification is an alert and the user taps the action button (or, if the device is locked, drags open the action slider), the app is woken up or launched. (If the user taps one of the custom actions you specify using the [`category`](uilocalnotification/category.md) property, the app is woken up or launched into the background.) In its [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method, the app delegate can obtain the `UILocalNotification` object from the launch options dictionary using the [`localNotification`](uiapplication/launchoptionskey/localnotification.md) key. The delegate can inspect the properties of the notification and, if the notification includes custom data in its [`userInfo`](uilocalnotification/userinfo.md) dictionary, it can access that data and process it accordingly. On the other hand, if the local notification only badges the app icon, and the user in response launches the app, the [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method is called, but no `UILocalNotification` object is included in the options dictionary. When the user selects a custom action, the app delegate’s [`application(_:handleActionWithIdentifier:for:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md) method is called to handle the action.

If the app is foremost and visible when the system delivers the notification, the app delegate’s [`application(_:didReceive:)`](uiapplicationdelegate/application(_:didreceive:).md) is called to process the notification. Use the information in the provided `UILocalNotification` object to decide what action to take. The system does not display any alerts, badge the app’s icon, or play any sounds when the app is already frontmost.

An app is responsible for managing the badge number displayed on its icon. For example, if a text-messaging app processes all incoming messages after receiving a local notification, it should remove the icon badge by setting the [`applicationIconBadgeNumber`](uiapplication/applicationiconbadgenumber.md) property of the [`UIApplication`](uiapplication.md) object to 0.

## Topics

### Scheduling a local notification
- [var fireDate: Date?](uilocalnotification/firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](uilocalnotification/repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](uilocalnotification/repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var region: CLRegion?](uilocalnotification/region.md)
  The geographic region that triggers the notification.
- [var regionTriggersOnce: Bool](uilocalnotification/regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.
### Composing the alert
- [var alertBody: String?](uilocalnotification/alertbody.md)
  The message displayed in the notification alert.
- [var alertAction: String?](uilocalnotification/alertaction.md)
  The title of the action button or slider.
- [var alertTitle: String?](uilocalnotification/alerttitle.md)
  A short description of the reason for the alert.
- [var hasAction: Bool](uilocalnotification/hasaction.md)
  A Boolean value that controls whether the notification shows or hides the alert action.
- [var alertLaunchImage: String?](uilocalnotification/alertlaunchimage.md)
  Identifies the image used as the launch image when the user taps (or slides) the action button (or slider).
- [var category: String?](uilocalnotification/category.md)
  The name of a group of actions to display in the alert.
### Configuring other parts of the notification
- [var applicationIconBadgeNumber: Int](uilocalnotification/applicationiconbadgenumber.md)
  The number to display as the app’s icon badge.
- [var soundName: String?](uilocalnotification/soundname.md)
  The name of the file containing the sound to play when an alert is displayed.
- [var userInfo: [AnyHashable : Any]?](uilocalnotification/userinfo.md)
  A dictionary for passing custom information to the notified app.
### Constants
- [Notification sound](notification-sound.md)
  The default system sound for local notifications.
### Initializers
- [init()](uilocalnotification/init.md)
- [init?(coder: NSCoder)](uilocalnotification/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification)*