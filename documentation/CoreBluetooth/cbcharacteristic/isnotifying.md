# isNotifying

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL isNotifying;
```

## Discussion

This value is [`true`](../../Swift/true.md) if you enabled notifications or indications for the characteristic by successfully calling the [`setNotifyValue(_:for:)`](../cbperipheral/setnotifyvalue%28_,for%29.md) method of the [`CBPeripheral`](../cbperipheral.md) class. In this case, the peripheral updates its connected central that whenever the characteristic’s value changes.

If the value of the property is [`false`](../../Swift/false.md), notifications (or indications) aren’t enabled for the characteristic, and the peripheral doesn’t update its connected central when the characteristic’s value changes.

## Topics

### Related Documentation
- [func setNotifyValue(Bool, for: CBCharacteristic)](../cbperipheral/setnotifyvalue%28_,for%29.md)
  Sets notifications or indications for the value of a specified characteristic.

## See Also

### Accessing Characteristic Data
- [var value: Data?](./value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](./descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](./properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](../cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isBroadcasted: Bool](./isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/isnotifying)*