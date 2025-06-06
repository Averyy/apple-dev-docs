# descriptors

**Framework**: Core Bluetooth  
**Kind**: property

A list of the descriptors discovered in this characteristic.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var descriptors: [CBDescriptor]? { get }
```

#### Discussion

The value of this property is an array of [`CBDescriptor`](cbdescriptor.md) objects that represent a characteristic’s descriptors. Characteristic descriptors provide more information about a characteristic’s value. For example, they may describe the value in human-readable form and describe how to format the value for presentation purposes. For more information about characteristic descriptors, see [`CBDescriptor`](cbdescriptor.md).

## See Also

- [var value: Data?](cbcharacteristic/value.md)
  The value of the characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isNotifying: Bool](cbcharacteristic/isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.
- [var isBroadcasted: Bool](cbcharacteristic/isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/descriptors)*