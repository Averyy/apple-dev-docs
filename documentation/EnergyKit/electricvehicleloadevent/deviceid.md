# deviceID

**Framework**: EnergyKit  
**Kind**: property

The device’s unique stable identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

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

- [let measurement: ElectricVehicleLoadEvent.ElectricalMeasurement](electricvehicleloadevent/measurement.md)
  The electricity consumption or generation of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/deviceid)*