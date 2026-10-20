# addNotificationListener

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Adds a function to call when a push notification occurs.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
void addNotificationListener(
	function listener
);
```

#### Discussion

To subscribe to changes and register for push notifications, see `saveSubscription` in the [`CloudKit.Database`](../cloudkit.database.md) class.

## Parameters

- `listener`: The function to call when a push notification occurs. The function must have a single argument that is a [`CloudKit.Notification`](../cloudkit.notification.md) object.

## See Also

### Receiving Notifications
- [removeNotificationListener](./removenotificationlistener.md)
  Removes a function to call when a push notification occurs.
- [registerForNotifications](./registerfornotifications.md)
  Registers to receive push notifications.
- [unregisterForNotifications](./unregisterfornotifications.md)
  Unregisters to receive push notifications.
- [isRegisteredForNotifications](./isregisteredfornotifications.md)
  Boolean value indicating whether this container is registered to receive push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/addnotificationlistener)*