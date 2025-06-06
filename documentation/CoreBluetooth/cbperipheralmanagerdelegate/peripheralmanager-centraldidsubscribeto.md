# peripheralManager(_:central:didSubscribeTo:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a remote central device subscribed to a characteristic’s value.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, central: CBCentral, didSubscribeTo characteristic: CBCharacteristic)
```

#### Discussion

Core Bluetooth invokes this method when a remote central device subscribes to the value of one of the local peripheral’s characteristics, by enabling notifications or indications on the characteristic’s value. When called, start sending the subscribed central updates as the characteristic’s value changes. To send updated characteristic values to subscribed centrals, use the [`updateValue(_:for:onSubscribedCentrals:)`](cbperipheralmanager/updatevalue(_:for:onsubscribedcentrals:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class.

## Parameters

- `peripheral`: The peripheral manager connected to the remote central.
- `central`: The remote central device that subscribed to the characteristic’s value.
- `characteristic`: The characteristic subscribed to.

## See Also

- [func peripheralManager(CBPeripheralManager, central: CBCentral, didUnsubscribeFrom: CBCharacteristic)](cbperipheralmanagerdelegate/peripheralmanager(_:central:didunsubscribefrom:).md)
  Tells the delegate that a remote central device unsubscribed from a characteristic’s value.
- [func peripheralManagerIsReady(toUpdateSubscribers: CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerisready(toupdatesubscribers:).md)
  Tells the delegate that a local peripheral device is ready to send characteristic value updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:central:didsubscribeto:))*