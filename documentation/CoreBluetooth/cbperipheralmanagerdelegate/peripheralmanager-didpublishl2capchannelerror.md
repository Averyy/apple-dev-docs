# peripheralManager(_:didPublishL2CAPChannel:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral manager created a listener for incoming L2CAP channel connections.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, didPublishL2CAPChannel PSM: CBL2CAPPSM, error: (any Error)?)
```

#### Discussion

The peripheral manager calls this method after you call [`publishL2CAPChannel(withEncryption:)`](cbperipheralmanager/publishl2capchannel(withencryption:).md). The `PSM` parameter contains the PSM assigned for the published channel.

## Parameters

- `peripheral`: The peripheral manager that published the channel.
- `PSM`: The Protocol/Service Multiplexer (PSM) of the published channel.
- `error`: The error that prevented publishing, or   if no error occurred.

## See Also

- [func peripheralManager(CBPeripheralManager, didUnpublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didunpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager removed a published service from the local system.
- [func peripheralManager(CBPeripheralManager, didOpen: CBL2CAPChannel?, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didopen:error:).md)
  Tells the delegate that the peripheral manager opened an L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:didpublishl2capchannel:error:))*