# isPassiveEntryAvailable(forVehicle:)

**Framework**: CarKey  
**Kind**: method

Returns a Boolean value that indicates whether passive entry is currently available for the specified vehicle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
func isPassiveEntryAvailable(forVehicle vehicleID: String) throws -> Bool
```

#### Return Value

`true` if passive entry is available, or `false` if the feature is not available.

## Parameters

- `vehicleID`: The target vehicle for the request. Choose the   vehicle from one of the session’s vehicle reports. Specify   the string in the   property of the corresponding   report.

## See Also

- [var vehicleReports: [VehicleReport]](carkeyremotecontrolsession/vehiclereports.md)
  The configuration details of the provisioned vehicles that match your company’s make.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/ispassiveentryavailable(forvehicle:))*