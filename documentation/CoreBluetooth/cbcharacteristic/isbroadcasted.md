# isBroadcasted

**Framework**: Core Bluetooth  
**Kind**: property

A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isBroadcasted: Bool { get }
```

#### Discussion

Don’t use this deprecated property.

## See Also

- [var value: Data?](cbcharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbcharacteristic/descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isNotifying: Bool](cbcharacteristic/isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/isbroadcasted)*