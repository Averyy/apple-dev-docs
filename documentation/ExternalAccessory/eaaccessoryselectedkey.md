# EAAccessorySelectedKey

**Framework**: External Accessory  
**Kind**: var

A key that indicates the accessory object that the user selected.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let EAAccessorySelectedKey: String
```

#### Discussion

The value assigned to this key is the [`EAAccessory`](eaaccessory.md) object that the user selected. This key is included in the info dictionary when the user pairs a Bluetooth accessory with the device using the Bluetooth picker.

## See Also

- [func registerForLocalNotifications()](eaaccessorymanager/registerforlocalnotifications.md)
  Begins the delivery of accessory-related notifications to the current application.
- [func unregisterForLocalNotifications()](eaaccessorymanager/unregisterforlocalnotifications.md)
  Stops the delivery of accessory-related notifications to the current application.
- [static let EAAccessoryDidConnect: NSNotification.Name](../foundation/nsnotification/name/1613827-eaaccessorydidconnect.md)
  A notification that the system sends when an accessory becomes connected and available for your application to use.
- [static let EAAccessoryDidDisconnect: NSNotification.Name](../foundation/nsnotification/name/1613901-eaaccessorydiddisconnect.md)
  A notification that is posted when an accessory is disconnected and no longer available for your application to use.
- [let EAAccessoryKey: String](eaaccessorykey.md)
  A key that indicates the accessory object whose status changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessoryselectedkey)*