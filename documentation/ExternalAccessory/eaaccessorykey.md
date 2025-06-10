# EAAccessoryKey

**Framework**: External Accessory  
**Kind**: var

A key that indicates the accessory object whose status changed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let EAAccessoryKey: String
```

#### Discussion

The [`EAAccessoryDidConnectNotification`](eaaccessorydidconnectnotification.md) and [`EAAccessoryDidDisconnectNotification`](eaaccessorydiddisconnectnotification.md) notifications contain this key in their userInfo dictionary. The value is an [`EAAccessory`](eaaccessory.md) object.

## See Also

- [func registerForLocalNotifications()](eaaccessorymanager/registerforlocalnotifications.md)
  Begins the delivery of accessory-related notifications to the current application.
- [func unregisterForLocalNotifications()](eaaccessorymanager/unregisterforlocalnotifications.md)
  Stops the delivery of accessory-related notifications to the current application.
- [static let EAAccessoryDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/EAAccessoryDidConnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/EAAccessoryDidDisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
- [let EAAccessorySelectedKey: String](eaaccessoryselectedkey.md)
  A key that indicates the accessory object that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorykey)*