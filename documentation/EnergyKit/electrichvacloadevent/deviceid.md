# deviceID

**Framework**: EnergyKit  
**Kind**: property

The device’s unique stable identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
let deviceID: String
```

#### Discussion

The max length is `64 UTF-8` characters. UUID strings are permitted. Ensure the identifier:

- Isn’t empty, and less than or equal to 64 characters.
- Uses only alphanumeric, space, hyphen, and apostrophe characters.
- Starts and ends with an alphanumeric character.

## See Also

- [let measurement: ElectricHVACLoadEvent.ElectricalMeasurement](electrichvacloadevent/measurement.md)
  The electricity consumption of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/deviceid)*