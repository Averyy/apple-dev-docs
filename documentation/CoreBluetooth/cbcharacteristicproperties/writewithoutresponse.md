# writeWithoutResponse

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

A property that indicates a peripheral can write the characteristic’s value, without a response to indicate that the write succeeded.

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
static var writeWithoutResponse: CBCharacteristicProperties { get }
```

```c
CBCharacteristicPropertyWriteWithoutResponse
```

## Discussion

Use the [`writeValue(_:for:type:)`](../cbperipheral/writevalue%28_,for,type%29.md) method of the [`CBPeripheral`](../cbperipheral.md) class to write to a characteristic’s value, using the [`CBCharacteristicWriteType.withoutResponse`](../cbcharacteristicwritetype/withoutresponse.md) constant as the parameter for `type`. If a characteristic has this property set, it doesn’t return an error to the central when it fails to write the characteristic’s value.

## See Also

### Characteristic Properties
- [static var broadcast: CBCharacteristicProperties](./broadcast.md)
  A property that indicates the characteristic can broadcast its value using a characteristic configuration descriptor.
- [static var read: CBCharacteristicProperties](./read.md)
  A property that indicates a peripheral can read the characteristic’s value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/writewithoutresponse)*