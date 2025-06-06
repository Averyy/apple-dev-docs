# extendedProperties

**Framework**: Core Bluetooth  
**Kind**: property

A property that indicates the characteristic defines additional properties in the extended properties descriptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var extendedProperties: CBCharacteristicProperties { get }
```

#### Discussion

This property is only available for a remote peripheral’s service’s characteristic. You can’t use this property with a local characteristic, that is, a [`CBMutableCharacteristic`](cbmutablecharacteristic.md) that you publish using the [`add(_:)`](cbperipheralmanager/add(_:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class.

## See Also

- [static var broadcast: CBCharacteristicProperties](cbcharacteristicproperties/broadcast.md)
  A property that indicates the characteristic can broadcast its value using a characteristic configuration descriptor.
- [static var read: CBCharacteristicProperties](cbcharacteristicproperties/read.md)
  A property that indicates a peripheral can read the characteristic’s value.
- [static var writeWithoutResponse: CBCharacteristicProperties](cbcharacteristicproperties/writewithoutresponse.md)
  A property that indicates a peripheral can write the characteristic’s value, without a response to indicate that the write succeeded.
- [static var write: CBCharacteristicProperties](cbcharacteristicproperties/write.md)
  A property that indicates a peripheral can write the characteristic’s value, with a response to indicate that the write succeeded.
- [static var notify: CBCharacteristicProperties](cbcharacteristicproperties/notify.md)
  A property that indicates the peripheral permits notifications of the characteristic’s value, without a response from the central to indicate receipt of the notification.
- [static var indicate: CBCharacteristicProperties](cbcharacteristicproperties/indicate.md)
  A property that indicates the peripheral permits notifications of the characteristic’s value, with a response from the central to indicate receipt of the notification.
- [static var authenticatedSignedWrites: CBCharacteristicProperties](cbcharacteristicproperties/authenticatedsignedwrites.md)
  A property that indicates the perhipheral allows signed writes of the characteristic’s value, without a response to indicate the write succeeded.
- [static var notifyEncryptionRequired: CBCharacteristicProperties](cbcharacteristicproperties/notifyencryptionrequired.md)
  A property that indicates that only trusted devices can enable notifications of the characteristic’s value.
- [static var indicateEncryptionRequired: CBCharacteristicProperties](cbcharacteristicproperties/indicateencryptionrequired.md)
  A property that indicates only trusted devices can enable indications of the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/extendedproperties)*