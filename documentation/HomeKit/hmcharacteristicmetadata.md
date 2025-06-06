# HMCharacteristicMetadata

**Framework**: HomeKit  
**Kind**: class

Metadata that describes a characteristic’s value and that may be useful for presentation purposes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMCharacteristicMetadata
```

#### Overview

Querying a characteristic’s metadata enables you to build a user interface that reflects the underlying units, minima, and maxima, and other aspects of the characteristic value.

## Topics

### Describing a characteristic
- [var manufacturerDescription: String?](hmcharacteristicmetadata/manufacturerdescription.md)
  A description of the characteristic provided by the accessory manufacturer.
### Bounding the value
- [var validValues: [NSNumber]?](hmcharacteristicmetadata/validvalues.md)
  The subset of valid values supported by the characteristic when the format is of type unsigned integer.
- [var minimumValue: NSNumber?](hmcharacteristicmetadata/minimumvalue.md)
  The minimum value for the characteristic.
- [var maximumValue: NSNumber?](hmcharacteristicmetadata/maximumvalue.md)
  The maximum value for the characteristic.
- [var stepValue: NSNumber?](hmcharacteristicmetadata/stepvalue.md)
  The minimum interval between values for the characteristic.
- [var maxLength: NSNumber?](hmcharacteristicmetadata/maxlength.md)
  The maximum number of UTF-8 characters allowed in a characteristic that uses a string format.
### Formatting the value
- [var format: String?](hmcharacteristicmetadata/format.md)
  The format of the values for the characteristic.
- [Characteristic Data Formats](characteristic-data-formats.md)
  Constants for identifying the data format of characteristic values.
### Specifying units
- [var units: String?](hmcharacteristicmetadata/units.md)
  The units of the characteristic value.
- [Characteristic Units](characteristic-units.md)
  Descriptions of the units of a characteristic.
### Initializers
- [init()](hmcharacteristicmetadata/init.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var metadata: HMCharacteristicMetadata?](hmcharacteristic/metadata.md)
  Metadata about the units and other properties of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata)*