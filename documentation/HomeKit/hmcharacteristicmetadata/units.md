# units

**Framework**: HomeKit  
**Kind**: property

The units of the characteristic value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var units: String? { get }
```

#### Discussion

The [`units`](hmcharacteristicmetadata/units.md) property tells you how to use the corresponding characteristic’s [`value`](hmcharacteristic/value.md) in calculations or how to format it for presentation. For example, you can extend the [`HMCharacteristic`](hmcharacteristic.md) class with a computed property that returns the appropriate symbol to accompany the value in printed output:

```swift
extension HMCharacteristic {
    var symbol: String {
        guard let units = metadata?.units else { return "" }

        switch units {
        case HMCharacteristicMetadataUnitsPercentage:              return "%"
        case HMCharacteristicMetadataUnitsPartsPerMillion:         return "ppm"
        case HMCharacteristicMetadataUnitsCelsius:                 return "°C"
        case HMCharacteristicMetadataUnitsFahrenheit:              return "°F"
        case HMCharacteristicMetadataUnitsSeconds:                 return "s"
        case HMCharacteristicMetadataUnitsLux:                     return "lx"
        case HMCharacteristicMetadataUnitsMicrogramsPerCubicMeter: return "μg/m³"
        case HMCharacteristicMetadataUnitsArcDegree:               return "°"
        default:                                                   return ""
        }
    }
}
```

See [`Characteristic Units`](characteristic-units.md) for the complete list of possible units.

## See Also

- [Characteristic Units](characteristic-units.md)
  Descriptions of the units of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/units)*