# vehicleReports

**Framework**: CarKey  
**Kind**: property

The configuration details of the provisioned vehicles that match your company’s make.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
var vehicleReports: [VehicleReport] { get throws }
```

#### Discussion

The system maintains a cache of provisioned vehicles and updates that information when the configuration details change.

## See Also

- [func isPassiveEntryAvailable(forVehicle: String) throws -> Bool](carkeyremotecontrolsession/ispassiveentryavailable(forvehicle:).md)
  Returns a Boolean value that indicates whether passive entry is currently available for the specified vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/vehiclereports)*