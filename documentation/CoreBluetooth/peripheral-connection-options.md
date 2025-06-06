# Peripheral Connection Options

**Framework**: Core Bluetooth

Keys used to pass options when connecting to a peripheral.

## Topics

### Options
- [let CBConnectPeripheralOptionEnableAutoReconnect: String](cbconnectperipheraloptionenableautoreconnect.md)
  A Boolean value that specifies whether the system automatically reconnects with a peripheral.
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

## See Also

- [func connect(CBPeripheral, options: [String : Any]?)](cbcentralmanager/connect(_:options:).md)
  Establishes a local connection to a peripheral.
- [func cancelPeripheralConnection(CBPeripheral)](cbcentralmanager/cancelperipheralconnection(_:).md)
  Cancels an active or pending local connection to a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-connection-options)*