# peripheralManager(_:central:didSubscribeTo:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) peripheralManager:(CBPeripheralManager *) peripheral central:(CBCentral *) central didSubscribeToCharacteristic:(CBCharacteristic *) characteristic;
```

## Discussion

Core Bluetooth invokes this method when a remote central device subscribes to the value of one of the local peripheral’s characteristics, by enabling notifications or indications on the characteristic’s value. When called, start sending the subscribed central updates as the characteristic’s value changes. To send updated characteristic values to subscribed centrals, use the [`updateValue(_:for:onSubscribedCentrals:)`](../cbperipheralmanager/updatevalue%28_,for,onsubscribedcentrals%29.md) method of the [`CBPeripheralManager`](../cbperipheralmanager.md) class.

## Parameters

- `peripheral`: The peripheral manager connected to the remote central.
- `central`: The remote central device that subscribed to the characteristic’s value.
- `characteristic`: The characteristic subscribed to.

## See Also

### Monitoring Subscriptions to Characteristic Values
- [func peripheralManager(CBPeripheralManager, central: CBCentral, didUnsubscribeFrom: CBCharacteristic)](./peripheralmanager%28_,central,didunsubscribefrom%29.md)
  Tells the delegate that a remote central device unsubscribed from a characteristic’s value.
- [func peripheralManagerIsReady(toUpdateSubscribers: CBPeripheralManager)](./peripheralmanagerisready%28toupdatesubscribers%29.md)
  Tells the delegate that a local peripheral device is ready to send characteristic value updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:central:didsubscribeto:))*