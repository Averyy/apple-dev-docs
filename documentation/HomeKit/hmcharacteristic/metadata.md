# metadata

**Framework**: HomeKit  
**Kind**: property

Metadata about the units and other properties of the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var metadata: HMCharacteristicMetadata? { get }
```

#### Discussion

You can typically infer a lot about a characteristic’s [`value`](hmcharacteristic/value.md) from its [`characteristicType`](hmcharacteristic/characteristictype.md), like if the value is a string, a number, or in some other format; what the units are; and what range of values to expect. To obtain this information explicitly, inspect the characteristic’s [`metadata`](hmcharacteristic/metadata.md), represented by an instance of the [`HMCharacteristicMetadata`](hmcharacteristicmetadata.md) class.

## See Also

- [class HMCharacteristicMetadata](hmcharacteristicmetadata.md)
  Metadata that describes a characteristic’s value and that may be useful for presentation purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/metadata)*