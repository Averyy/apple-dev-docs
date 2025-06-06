# peripheralManagerIsReady(toUpdateSubscribers:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a local peripheral device is ready to send characteristic value updates.

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
optional func peripheralManagerIsReady(toUpdateSubscribers peripheral: CBPeripheralManager)
```

#### Discussion

When a call to the [`updateValue(_:for:onSubscribedCentrals:)`](cbperipheralmanager/updatevalue(_:for:onsubscribedcentrals:).md) method fails because the underlying queue used to transmit the updated characteristic value is full, Core Bluetooth calls the [`peripheralManagerIsReady(toUpdateSubscribers:)`](cbperipheralmanagerdelegate/peripheralmanagerisready(toupdatesubscribers:).md) method when more space in the transmit queue becomes available. You can then implement this delegate method to resend the value.

## Parameters

- `peripheral`: The peripheral manager that sends characteristic value updates.

## See Also

- [func peripheralManager(CBPeripheralManager, central: CBCentral, didSubscribeTo: CBCharacteristic)](cbperipheralmanagerdelegate/peripheralmanager(_:central:didsubscribeto:).md)
  Tells the delegate that a remote central device subscribed to a characteristic’s value.
- [func peripheralManager(CBPeripheralManager, central: CBCentral, didUnsubscribeFrom: CBCharacteristic)](cbperipheralmanagerdelegate/peripheralmanager(_:central:didunsubscribefrom:).md)
  Tells the delegate that a remote central device unsubscribed from a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanagerisready(toupdatesubscribers:))*