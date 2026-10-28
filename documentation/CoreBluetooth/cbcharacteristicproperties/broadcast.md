# broadcast

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

A property that indicates the characteristic can broadcast its value using a characteristic configuration descriptor.

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
static var broadcast: CBCharacteristicProperties { get }
```

```c
CBCharacteristicPropertyBroadcast
```

## Discussion

Don’t use this property for local characteristics published with the [`add(_:)`](../cbperipheralmanager/add%28_%29.md) method of the [`CBPeripheralManager`](../cbperipheralmanager.md) class. You can’t use this property when you initialize a new [`CBMutableCharacteristic`](../cbmutablecharacteristic.md) object with the [`init(type:properties:value:permissions:)`](../cbmutablecharacteristic/init%28type,properties,value,permissions%29.md) method of the [`CBMutableCharacteristic`](../cbmutablecharacteristic.md) class.

## See Also

### Characteristic Properties
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
- [static var extendedProperties: CBCharacteristicProperties](./extendedproperties.md)
  A property that indicates the characteristic defines additional properties in the extended properties descriptor.
- [static var notifyEncryptionRequired: CBCharacteristicProperties](./notifyencryptionrequired.md)
  A property that indicates that only trusted devices can enable notifications of the characteristic’s value.
- [static var indicateEncryptionRequired: CBCharacteristicProperties](./indicateencryptionrequired.md)
  A property that indicates only trusted devices can enable indications of the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/broadcast)*