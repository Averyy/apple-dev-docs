# isBroadcasted

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.13
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var isBroadcasted: Bool { get }
```

```objc
@property (readonly) BOOL isBroadcasted;
```

## Discussion

Don’t use this deprecated property.

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
- [var isNotifying: Bool](./isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/isbroadcasted)*