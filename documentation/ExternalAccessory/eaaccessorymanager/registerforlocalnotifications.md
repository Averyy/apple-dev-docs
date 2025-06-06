# registerForLocalNotifications()

**Framework**: External Accessory  
**Kind**: method

Begins the delivery of accessory-related notifications to the current application.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func registerForLocalNotifications()
```

#### Discussion

Call this method to be notified when an accessory becomes connected or disconnected. The system does not send [`EAAccessoryDidConnectNotification`](eaaccessorydidconnectnotification.md) and [`EAAccessoryDidDisconnectNotification`](eaaccessorydiddisconnectnotification.md) notifications automatically, so calling this method lets the system know that your application wants to receive them. Typically, you would call this method only once early in your application, either before or after configuring your notification observers. When you no longer need to monitor these notifications, you should call the matching [`unregisterForLocalNotifications()`](eaaccessorymanager/unregisterforlocalnotifications().md) method.

You can configure your notification observers either before or after calling this method. Because the shared accessory manager is the only object that sends accessory-related notifications, specifying that object or `nil` for the notification sender has the same outcome.

## See Also

- [func unregisterForLocalNotifications()](eaaccessorymanager/unregisterforlocalnotifications.md)
  Stops the delivery of accessory-related notifications to the current application.
- [static let EAAccessoryDidConnect: NSNotification.Name](../foundation/nsnotification/name/1613827-eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](../foundation/nsnotification/name/1613901-eaaccessorydiddisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
- [let EAAccessoryKey: String](eaaccessorykey.md)
  A key that indicates the accessory object whose status changed.
- [let EAAccessorySelectedKey: String](eaaccessoryselectedkey.md)
  A key that indicates the accessory object that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/registerforlocalnotifications())*