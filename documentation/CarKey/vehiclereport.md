# VehicleReport

**Framework**: CarKey  
**Kind**: struct

A type that contains information about a vehicle configured for remote keyless entry in the user’s Apple Wallet.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct VehicleReport
```

#### Overview

A `VehicleReport` type provides information about a vehicle you manufacture. The system generates a vehicle report for each vehicle that matches your company’s make, and that the owner configured in their Apple Wallet. Use a vehicle report to get information about the vehicle, such as whether it’s currently connected and able to receive commands. You can also use the report to determine which vehicle features you can operate from your app.

A vehicle can optionally attach proprietary data to one of its function identifiers. You might use this data to support additional features related to that vehicle feature. For example, you might want to attach a unique security code to the door lock function. Use the vehicle report to retrieve any data your vehicle sends. If the vehicle sends new data, the system updates the report and notifies your session delegate.

## Topics

### Getting the Vehicle Details
- [let identifier: String](vehiclereport/identifier.md)
  The string you use to identify the vehicle when making requests.
- [var isConnected: Bool](vehiclereport/isconnected.md)
  A Boolean value that indicates whether the vehicle is currently connected over Bluetooth.
### Getting the Vehicle’s Supported Functions
- [var supportedFunctions: [FunctionIdentifier]](vehiclereport/supportedfunctions.md)
  An array of function identifiers that indicates the features the vehicle supports, populated only after the first BLE connection with the vehicle.
- [func status(for: FunctionIdentifier) throws -> FunctionStatus?](vehiclereport/status(for:).md)
  Returns the current status of the specified vehicle function.
- [struct FunctionStatus](functionstatus.md)
  A value that the vehicle can return to indicate the status of a particular vehicle feature.
### Fetching Data Sent by the Vehicle
- [func proprietaryData(for: FunctionIdentifier) throws -> Data?](vehiclereport/proprietarydata(for:).md)
  Retrieves the proprietary data associated with one of the vehicle’s functions.

## See Also

- [class CarKeyRemoteControl](carkeyremotecontrol.md)
  The object you use to start a new vehicle-related session.
- [class CarKeyRemoteControlSession](carkeyremotecontrolsession.md)
  The object that manages communication with the vehicles you manufacture.
- [protocol CarKeyRemoteControlSessionDelegate](carkeyremotecontrolsessiondelegate.md)
  An interface you use to receive session- and vehicle-related information from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/vehiclereport)*