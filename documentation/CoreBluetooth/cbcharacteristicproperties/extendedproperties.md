# extendedProperties

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

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

```c
CBCharacteristicPropertyExtendedProperties
```

#### Discussion

This property is only available for a remote peripheral’s service’s characteristic. You can’t use this property with a local characteristic, that is, a [`CBMutableCharacteristic`](../cbmutablecharacteristic.md) that you publish using the [`add(_:)`](../cbperipheralmanager/add%28_%29.md) method of the [`CBPeripheralManager`](../cbperipheralmanager.md) class.

## See Also

### Characteristic Properties
- [static var broadcast: CBCharacteristicProperties](./broadcast.md)
  A property that indicates the characteristic can broadcast its value using a characteristic configuration descriptor.
- [static var read: CBCharacteristicProperties](./read.md)
  A property that indicates a peripheral can read the characteristic’s value.
- [static var writeWithoutResponse: CBCharacteristicProperties](./writewithoutresponse.md)
  A property that indicates a peripheral can write the characteristic’s value, without a response to indicate that the write succeeded.
- [static var write: CBCharacteristicProperties](./write.md)
  A property that indicates a peripheral can write the characteristic’s value, with a response to indicate that the write succeeded.
- [static var notify: CBCharacteristicProperties](./notify.md)
  A property that indicates the peripheral permits notifications of the characteristic’s value, without a response from the central to indicate receipt of the notification.
- [static var indicate: CBCharacteristicProperties](./indicate.md)
  A property that indicates the peripheral permits notifications of the characteristic’s value, with a response from the central to indicate receipt of the notification.
- [static var authenticatedSignedWrites: CBCharacteristicProperties](./authenticatedsignedwrites.md)
  A property that indicates the perhipheral allows signed writes of the characteristic’s value, without a response to indicate the write succeeded.
- [static var notifyEncryptionRequired: CBCharacteristicProperties](./notifyencryptionrequired.md)
  A property that indicates that only trusted devices can enable notifications of the characteristic’s value.
- [static var indicateEncryptionRequired: CBCharacteristicProperties](./indicateencryptionrequired.md)
  A property that indicates only trusted devices can enable indications of the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/extendedproperties)*