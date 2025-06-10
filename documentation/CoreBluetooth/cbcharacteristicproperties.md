# CBCharacteristicProperties

**Framework**: Core Bluetooth  
**Kind**: struct

Values that represent the possible properties of a characteristic.

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
struct CBCharacteristicProperties
```

#### Overview

Since you can combine characteristic properties, a characteristic may have multiple property values set.

## Topics

### Creating a Characteristic Properties Instance
- [init(rawValue: UInt)](cbcharacteristicproperties/init(rawvalue:).md)
  Creates a characteristic properties instance from the given raw value.
### Characteristic Properties
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
- [static var extendedProperties: CBCharacteristicProperties](cbcharacteristicproperties/extendedproperties.md)
  A property that indicates the characteristic defines additional properties in the extended properties descriptor.
- [static var notifyEncryptionRequired: CBCharacteristicProperties](cbcharacteristicproperties/notifyencryptionrequired.md)
  A property that indicates that only trusted devices can enable notifications of the characteristic’s value.
- [static var indicateEncryptionRequired: CBCharacteristicProperties](cbcharacteristicproperties/indicateencryptionrequired.md)
  A property that indicates only trusted devices can enable indications of the characteristic’s value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var value: Data?](cbcharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbcharacteristic/descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [var isNotifying: Bool](cbcharacteristic/isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.
- [var isBroadcasted: Bool](cbcharacteristic/isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties)*