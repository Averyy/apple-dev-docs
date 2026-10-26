# EAAccessoryDidDisconnectNotification

**Framework**: External Accessory  
**Kind**: var  
**Role**: Global Variable

A notification that is posted when an accessory is disconnected and no longer available for your application to use.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const EAAccessoryDidDisconnectNotification;
```

#### Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [`EAAccessoryKey`](./eaaccessorykey.md), whose value is the [`EAAccessory`](./eaaccessory.md) object representing the accessory that was disconnected. Before delivery of this notification can occur, you must call the [`registerForLocalNotifications()`](./eaaccessorymanager/registerforlocalnotifications%28%29.md) method to let the system know you are interested in receiving this notification.

If your accessory manager has a delegate, the delegate can use the [`accessoryDidDisconnect(_:)`](./eaaccessorydelegate/accessorydiddisconnect%28_%29.md) method to receive this notification instead.

## See Also

### Managing Connection Status Changes
- [func registerForLocalNotifications()](./eaaccessorymanager/registerforlocalnotifications%28%29.md)
  Begins the delivery of accessory-related notifications to the current application.
- [func unregisterForLocalNotifications()](./eaaccessorymanager/unregisterforlocalnotifications%28%29.md)
  Stops the delivery of accessory-related notifications to the current application.
- [EAAccessoryDidConnectNotification](./eaaccessorydidconnectnotification.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [let EAAccessoryKey: String](./eaaccessorykey.md)
  A key that indicates the accessory object whose status changed.
- [let EAAccessorySelectedKey: String](./eaaccessoryselectedkey.md)
  A key that indicates the accessory object that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorydiddisconnectnotification)*