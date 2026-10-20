# properties

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The properties of the characteristic.

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
var properties: CBCharacteristicProperties { get }
```

```objc
@property (nonatomic, readonly) CBCharacteristicProperties properties;
```

#### Discussion

The properties of a characteristic determine the access to and use of the characteristic’s value and descriptors. For a list of the possible values representing the properties of a characteristic, see [`CBCharacteristicProperties`](../cbcharacteristicproperties.md).

## See Also

### Accessing Characteristic Data
- [var value: Data?](./value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](./descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [struct CBCharacteristicProperties](../cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isNotifying: Bool](./isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.
- [var isBroadcasted: Bool](./isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/properties)*