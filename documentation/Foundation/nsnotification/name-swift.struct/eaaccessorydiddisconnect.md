# EAAccessoryDidDisconnect

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [`EAAccessoryKey`](../../../ExternalAccessory/eaaccessorykey.md), whose value is the [`EAAccessory`](../../../ExternalAccessory/eaaccessory.md) object representing the accessory that was disconnected. Before delivery of this notification can occur, you must call the [`registerForLocalNotifications()`](../../../ExternalAccessory/eaaccessorymanager/registerforlocalnotifications%28%29.md) method to let the system know you are interested in receiving this notification.

If your accessory manager has a delegate, the delegate can use the [`accessoryDidDisconnect(_:)`](../../../ExternalAccessory/eaaccessorydelegate/accessorydiddisconnect%28_%29.md) method to receive this notification instead.

## See Also

### External Accessory
- [static let EAAccessoryDidConnect: NSNotification.Name](./eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect)*