# UIAccelerometer

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that lets you register to receive acceleration-related data from the onboard hardware.

> **Deprecated**: Use the [Core Motion](../CoreMotion/CoreMotion.md) framework instead.

## Declaration

```objc
@interface UIAccelerometer : NSObject
```

## Overview

As a device moves, its hardware reports linear acceleration changes along the primary axes in three-dimensional space. You can use this data to detect both the current orientation of the device (relative to the ground) and any instantaneous changes to that orientation. You might use instantaneous changes as input to a game or to initiate some action in your application.

You don’t create accelerometer objects directly. Instead, you use the shared `UIAccelerometer` object to specify the interval at which you want to receive events and then set its [`delegate`](./uiaccelerometer/delegate.md) property. Upon assigning your delegate object, the accelerometer object begins delivering acceleration events to your delegate immediately at the specified interval. Events are always delivered on the main thread of your application.

The maximum frequency for accelerometer updates is based on the available hardware. You can request updates less frequently but can’t request them more frequently than the hardware maximum. Once you assign your delegate, however, updates are delivered regularly at the frequency you requested, whether or not the acceleration data actually changed. Your delegate is responsible for filtering out any unwanted updates and for ensuring that the amount of change is significant enough to warrant taking action.

For more information about the data delivered to your observer, see [`UIAcceleration`](./uiacceleration.md). For information about implementing your delegate object, see [`UIAccelerometerDelegate`](./uiaccelerometerdelegate.md).

## Topics

### Getting the shared accelerometer object
- [+ sharedAccelerometer](./uiaccelerometer/sharedaccelerometer.md)
  Returns the shared accelerometer object for the system.
### Accessing the accelerometer properties
- [updateInterval](./uiaccelerometer/updateinterval.md)
  The interval at which to deliver acceleration data to the delegate.
- [delegate](./uiaccelerometer/delegate.md)
  The delegate object you want to receive acceleration events.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Deprecated classes
- [UIAcceleration](./uiacceleration.md)
  An acceleration event that represents immediate, three-dimensional acceleration data.
- [class UIActionSheet](./uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](./uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](./uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](./uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](./uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](./uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](./uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](./uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](./uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](./uipreviewaction.md)
  A preview action, or *peek quick action*, that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](./uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UISearchDisplayController](./uisearchdisplaycontroller.md)
  An object that manages the display of a search bar, along with a table view that displays search results.
- [class UIStoryboardPopoverSegue](./uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIWebView](./uiwebview.md)
  A view that embeds web content in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccelerometer)*