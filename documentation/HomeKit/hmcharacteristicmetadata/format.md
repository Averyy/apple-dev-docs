# format

**Framework**: HomeKit  
**Kind**: property

The format of the values for the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var format: String? { get }
```

#### Discussion

The [`format`](hmcharacteristicmetadata/format.md) property tells you what kind of data the characteristic’s [`value`](hmcharacteristic/value.md) contains. For example, you can extend the [`HMCharacteristic`](hmcharacteristic.md) class with a computed property that reports whether a given characteristic is a floating point number:

```swift
extension HMCharacteristic {
    var isFloat: Bool {
        return metadata?.format == HMCharacteristicMetadataFormatFloat
    }
}
```

See [`Characteristic Data Formats`](characteristic-data-formats.md) for the list of possible formats.

## See Also

- [Characteristic Data Formats](characteristic-data-formats.md)
  Constants for identifying the data format of characteristic values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/format)*