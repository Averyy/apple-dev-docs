# value

**Framework**: Core Bluetooth  
**Kind**: property

The value of the characteristic.

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
var value: Data? { get }
```

#### Discussion

This property contains the value of the characteristic. For example, a temperature measurement characteristic of a health thermometer service may have a value that indicates a temperature in Celsius.

## See Also

- [var descriptors: [CBDescriptor]?](cbcharacteristic/descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isNotifying: Bool](cbcharacteristic/isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.
- [var isBroadcasted: Bool](cbcharacteristic/isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/value)*