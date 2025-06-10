# EAAccessoryDidDisconnect

**Framework**: Foundation  
**Kind**: property

A notification that is posted when an accessory is disconnected and no longer available for your application to use.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let EAAccessoryDidDisconnect: NSNotification.Name
```

#### Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [`EAAccessoryKey`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryKey), whose value is the [`EAAccessory`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessory) object representing the accessory that was disconnected. Before delivery of this notification can occur, you must call the [`registerForLocalNotifications()`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryManager/registerForLocalNotifications()) method to let the system know you are interested in receiving this notification.

If your accessory manager has a delegate, the delegate can use the [`accessoryDidDisconnect(_:)`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryDelegate/accessoryDidDisconnect(_:)) method to receive this notification instead.

## See Also

- [static let EAAccessoryDidConnect: NSNotification.Name](nsnotification/name-swift.struct/eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect)*