# EAAccessoryDidConnectNotification

**Framework**: External Accessory  
**Kind**: var  
**Role**: Global Variable

A notification that the system sends when an accessory becomes connected and available for your application to use.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const EAAccessoryDidConnectNotification;
```

## Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [`EAAccessoryKey`](./eaaccessorykey.md), whose value is an [`EAAccessory`](./eaaccessory.md) object representing the accessory that is now connected. If a Bluetooth accessory was selected by the user in the Bluetooth picker, this dictionary contains the [`EAAccessorySelectedKey`](./eaaccessoryselectedkey.md) key. Before delivery of this notification can occur, you must call the [`registerForLocalNotifications()`](./eaaccessorymanager/registerforlocalnotifications%28%29.md) method to let the system know you are interested in receiving this notification.

After receiving this notification, always check the [`protocolStrings`](./eaaccessory/protocolstrings.md) array of the newly connected accessory object to verify that the required protocol is present before trying to open a session. In some cases, the system may send the connection notification before authentication has completed, resulting in an empty [`protocolStrings`](./eaaccessory/protocolstrings.md) array and a subsequent disconnection message. If this happens, the system sends another connection message later, when authentication succeeds.

> ❗ **Important**:  iPhone and iPad apps running on Macs with Apple silicon never receive this notification.

## See Also

### Managing Connection Status Changes
- [func registerForLocalNotifications()](./eaaccessorymanager/registerforlocalnotifications%28%29.md)
  Begins the delivery of accessory-related notifications to the current application.
- [func unregisterForLocalNotifications()](./eaaccessorymanager/unregisterforlocalnotifications%28%29.md)
  Stops the delivery of accessory-related notifications to the current application.
- [EAAccessoryDidDisconnectNotification](./eaaccessorydiddisconnectnotification.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
- [let EAAccessoryKey: String](./eaaccessorykey.md)
  A key that indicates the accessory object whose status changed.
- [let EAAccessorySelectedKey: String](./eaaccessoryselectedkey.md)
  A key that indicates the accessory object that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorydidconnectnotification)*