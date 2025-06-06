# CBConnectPeripheralOptionEnableTransportBridgingKey

**Framework**: Core Bluetooth  
**Kind**: var

An option to bridge classic Bluetooth technology profiles, if already connected over Bluetooth Low Energy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let CBConnectPeripheralOptionEnableTransportBridgingKey: String
```

#### Discussion

This option tells the system to connect non-GATT profiles on classic Bluetooth devices, if there is a low energy GATT connection to the same device.

The value associated with this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) as a Boolean value. A `true` value instructs the system to bring up classic transport profiles when a low energy transport peripheral connects. A `false` value tells the system not to use the profiles.

## See Also

- [let CBConnectPeripheralOptionEnableAutoReconnect: String](cbconnectperipheraloptionenableautoreconnect.md)
  A Boolean value that specifies whether the system automatically reconnects with a peripheral.
- [let CBConnectPeripheralOptionNotifyOnConnectionKey: String](cbconnectperipheraloptionnotifyonconnectionkey.md)
  A Boolean value that specifies whether the system should display an alert when connecting a peripheral in the background.
- [let CBConnectPeripheralOptionNotifyOnDisconnectionKey: String](cbconnectperipheraloptionnotifyondisconnectionkey.md)
  A Boolean value that specifies whether the system should display an alert when disconnecting a peripheral in the background.
- [let CBConnectPeripheralOptionNotifyOnNotificationKey: String](cbconnectperipheraloptionnotifyonnotificationkey.md)
  A Boolean value that specifies whether the system should display an alert for any notification sent by a peripheral.
- [let CBConnectPeripheralOptionRequiresANCS: String](cbconnectperipheraloptionrequiresancs.md)
  An option to require Apple Notification Center Service (ANCS) when connecting a device.
- [let CBConnectPeripheralOptionStartDelayKey: String](cbconnectperipheraloptionstartdelaykey.md)
  An option that indicates a delay before the system makes a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionenabletransportbridgingkey)*