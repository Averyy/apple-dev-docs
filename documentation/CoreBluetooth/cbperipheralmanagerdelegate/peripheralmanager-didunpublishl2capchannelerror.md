# peripheralManager(_:didUnpublishL2CAPChannel:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral manager removed a published service from the local system.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func peripheralManager(_ peripheral: CBPeripheralManager, didUnpublishL2CAPChannel PSM: CBL2CAPPSM, error: (any Error)?)
```

#### Discussion

The peripheral manager calls this method after you call [`unpublishL2CAPChannel(_:)`](cbperipheralmanager/unpublishl2capchannel(_:).md).

## Parameters

- `peripheral`: The peripheral manager that stopped publishing.
- `PSM`: The Protocol/Service Multiplexer (PSM) of the channel that was unpublished.
- `error`: The error that occurred, or   if no error occurred.

## See Also

- [func peripheralManager(CBPeripheralManager, didPublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager created a listener for incoming L2CAP channel connections.
- [func peripheralManager(CBPeripheralManager, didOpen: CBL2CAPChannel?, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didopen:error:).md)
  Tells the delegate that the peripheral manager opened an L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:didunpublishl2capchannel:error:))*