# properties

**Framework**: HomeKit  
**Kind**: property

An array of properties that describe the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var properties: [String] { get }
```

#### Discussion

Test a characteristic’s [`properties`](hmcharacteristic/properties.md) array for any of the constants listed in [`Characteristic Properties`](characteristic-properties.md) to learn something about the corresponding characteristic. For example, you can create a readability Boolean in an extension to the [`HMCharacteristic`](hmcharacteristic.md) class by testing for [`HMCharacteristicPropertyReadable`](hmcharacteristicpropertyreadable.md):

```swift
extension HMCharacteristic {
    var isReadable: Bool {
        return properties.contains(HMCharacteristicPropertyReadable)
    }
}
```

## See Also

- [Characteristic Properties](characteristic-properties.md)
  The properties that characteristics can have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/properties)*