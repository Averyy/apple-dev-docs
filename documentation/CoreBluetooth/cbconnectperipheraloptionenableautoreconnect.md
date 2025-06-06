# CBConnectPeripheralOptionEnableAutoReconnect

**Framework**: Core Bluetooth  
**Kind**: var

A Boolean value that specifies whether the system automatically reconnects with a peripheral.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
let CBConnectPeripheralOptionEnableAutoReconnect: String
```

#### Discussion

After a peripheral device connects, this setting enables the system to initiate a connection to the peer device automatically when the link drops. The system uses [`centralManager(_:didDisconnectPeripheral:timestamp:isReconnecting:error:)`](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:timestamp:isreconnecting:error:).md) to notify the caller about the disconnection.

## See Also

- [let CBConnectPeripheralOptionEnableTransportBridgingKey: String](cbconnectperipheraloptionenabletransportbridgingkey.md)
  An option to bridge classic Bluetooth technology profiles, if already connected over Bluetooth Low Energy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionenableautoreconnect)*