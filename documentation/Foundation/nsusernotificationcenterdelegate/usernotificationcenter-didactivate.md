# userNotificationCenter(_:didActivate:)

**Framework**: Foundation  
**Kind**: method

Sent to the delegate when a user clicks on a user notification presented by the user notification center.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func userNotificationCenter(_ center: NSUserNotificationCenter, didActivate notification: NSUserNotification)
```

#### Discussion

This would be a good time to take action in response to user interacting with a specific notification.

To take an action when your application is launched as a result of a user clicking on a notification, be sure to implement the [`applicationDidFinishLaunching(_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationDidFinishLaunching(_:)) method in the application class that implements the [`NSApplicationDelegate`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate) protocol. The notification parameter to that method has a `userInfo` dictionary, and if that dictionary has the `NSApplicationLaunchUserNotificationKey` key. The value of that key is the [`NSUserNotification`](nsusernotification.md) object that caused the application to launch. The `NSUserNotification` object is delivered to the `NSApplication` delegate because that message will be sent before your application has a chance to set a delegate for the `NSUserNotificationCenter`.

## Parameters

- `center`: The user notification center.
- `notification`: The user notification object.

## See Also

- [func userNotificationCenter(NSUserNotificationCenter, didDeliver: NSUserNotification)](nsusernotificationcenterdelegate/usernotificationcenter(_:diddeliver:).md)
  Sent to the delegate when a notification delivery date has arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:))*