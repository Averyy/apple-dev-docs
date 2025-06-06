# updateValue(_:for:onSubscribedCentrals:)

**Framework**: Core Bluetooth  
**Kind**: method

Send an updated characteristic value to one or more subscribed centrals, using a notification or indication.

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
func updateValue(_ value: Data, for characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool
```

#### Return Value

This value is [`true`](https://developer.apple.com/documentation/swift/true) if the update is successfully sent to the subscribed central or centrals. [`false`](https://developer.apple.com/documentation/swift/false) if the update isn’t successfully sent because the underlying transmit queue is full.

#### Discussion

You use this method to send updates of a characteristic’s value—through a notification or indication—to selected centrals that have subscribed to that characteristic’s value. If the method returns [`false`](https://developer.apple.com/documentation/swift/false) because the underlying transmit queue is full, the peripheral manager calls the [`peripheralManagerIsReady(toUpdateSubscribers:)`](cbperipheralmanagerdelegate/peripheralmanagerisready(toupdatesubscribers:).md) method of its delegate object when more space in the transmit queue becomes available. After you receive this delegate method callback, you may resend the update.

If the length of the `value` parameter exceeds the length of the [`maximumUpdateValueLength`](cbcentral/maximumupdatevaluelength.md) property of a subscribed [`CBCentral`](cbcentral.md), the `value` parameter truncates accordingly.

## Parameters

- `value`: The characteristic value you want to send via a notification or indication.
- `characteristic`: The characteristic whose value has changed.
- `centrals`: A list of centrals (represented by   objects) that have subscribed to receive updates of the characteristic’s value. If  , the manager updates all subscribed centrals. The manager ignores any centrals that haven’t subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/updatevalue(_:for:onsubscribedcentrals:))*