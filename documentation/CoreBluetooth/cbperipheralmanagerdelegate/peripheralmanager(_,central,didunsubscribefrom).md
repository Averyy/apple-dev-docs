# peripheralManager(_:central:didUnsubscribeFrom:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a remote central device unsubscribed from a characteristic’s value.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, central: CBCentral, didUnsubscribeFrom characteristic: CBCharacteristic)
```

```objc
- (void) peripheralManager:(CBPeripheralManager *) peripheral central:(CBCentral *) central didUnsubscribeFromCharacteristic:(CBCharacteristic *) characteristic;
```

#### Discussion

Core Bluetooth calls this method when a remote central device unsubscribes from the value of one of the local peripheral’s characteristics, by disabling notifications or indications on the characteristic’s value. When called, stop sending the subscribed central updates of updates to the characteristic’s value.

## Parameters

- `peripheral`: The peripheral manager connected to the remote central.
- `central`: The remote central device that subscribed to the characteristic’s value.
- `characteristic`: The characteristic unsubscribed from.

## See Also

### Monitoring Subscriptions to Characteristic Values
- [func peripheralManager(CBPeripheralManager, central: CBCentral, didSubscribeTo: CBCharacteristic)](./peripheralmanager%28_,central,didsubscribeto%29.md)
  Tells the delegate that a remote central device subscribed to a characteristic’s value.
- [func peripheralManagerIsReady(toUpdateSubscribers: CBPeripheralManager)](./peripheralmanagerisready%28toupdatesubscribers%29.md)
  Tells the delegate that a local peripheral device is ready to send characteristic value updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:central:didunsubscribefrom:))*