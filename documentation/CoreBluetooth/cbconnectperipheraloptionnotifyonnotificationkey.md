# CBConnectPeripheralOptionNotifyOnNotificationKey

**Framework**: Core Bluetooth  
**Kind**: var

A Boolean value that specifies whether the system should display an alert for any notification sent by a peripheral.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBConnectPeripheralOptionNotifyOnNotificationKey: String
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the system displays an alert for all notifications received from a given peripheral while the app is suspended.

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. This key is useful for apps that haven’t specified the `bluetooth-central` background mode and can’t display their own alert. If more than one app requests a notification for a given peripheral, the one that was most recently in the foreground receives the alert. If the key isn’t specified, the default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [let CBConnectPeripheralOptionEnableAutoReconnect: String](cbconnectperipheraloptionenableautoreconnect.md)
  A Boolean value that specifies whether the system automatically reconnects with a peripheral.
- [let CBConnectPeripheralOptionEnableTransportBridgingKey: String](cbconnectperipheraloptionenabletransportbridgingkey.md)
  An option to bridge classic Bluetooth technology profiles, if already connected over Bluetooth Low Energy.
- [let CBConnectPeripheralOptionNotifyOnConnectionKey: String](cbconnectperipheraloptionnotifyonconnectionkey.md)
  A Boolean value that specifies whether the system should display an alert when connecting a peripheral in the background.
- [let CBConnectPeripheralOptionNotifyOnDisconnectionKey: String](cbconnectperipheraloptionnotifyondisconnectionkey.md)
  A Boolean value that specifies whether the system should display an alert when disconnecting a peripheral in the background.
- [let CBConnectPeripheralOptionRequiresANCS: String](cbconnectperipheraloptionrequiresancs.md)
  An option to require Apple Notification Center Service (ANCS) when connecting a device.
- [let CBConnectPeripheralOptionStartDelayKey: String](cbconnectperipheraloptionstartdelaykey.md)
  An option that indicates a delay before the system makes a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonnotificationkey)*