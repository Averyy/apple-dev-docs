# isNotifying

**Framework**: Core Bluetooth  
**Kind**: property

A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.

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
var isNotifying: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if you enabled notifications or indications for the characteristic by successfully calling the [`setNotifyValue(_:for:)`](cbperipheral/setnotifyvalue(_:for:).md) method of the [`CBPeripheral`](cbperipheral.md) class. In this case, the peripheral updates its connected central that whenever the characteristic’s value changes.

If the value of the property is [`false`](https://developer.apple.com/documentation/Swift/false), notifications (or indications) aren’t enabled for the characteristic, and the peripheral doesn’t update its connected central when the characteristic’s value changes.

## Topics

### Related Documentation
- [func setNotifyValue(Bool, for: CBCharacteristic)](cbperipheral/setnotifyvalue(_:for:).md)
  Sets notifications or indications for the value of a specified characteristic.

## See Also

- [var value: Data?](cbcharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbcharacteristic/descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isBroadcasted: Bool](cbcharacteristic/isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/isnotifying)*