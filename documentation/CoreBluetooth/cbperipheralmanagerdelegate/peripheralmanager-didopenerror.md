# peripheralManager(_:didOpen:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral manager opened an L2CAP channel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func peripheralManager(_ peripheral: CBPeripheralManager, didOpen channel: CBL2CAPChannel?, error: (any Error)?)
```

#### Discussion

The peripheral manager calls this method after you call [`publishL2CAPChannel(withEncryption:)`](cbperipheralmanager/publishl2capchannel(withencryption:).md).

## Parameters

- `peripheral`: The peripheral manager that opened the channel.
- `channel`: The channel opened by the manager.
- `error`: The error that occurred, or   if no error occurred.

## See Also

- [func peripheralManager(CBPeripheralManager, didPublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager created a listener for incoming L2CAP channel connections.
- [func peripheralManager(CBPeripheralManager, didUnpublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didunpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager removed a published service from the local system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:didopen:error:))*