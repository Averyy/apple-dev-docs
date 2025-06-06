# sendPassthroughData(_:toVehicle:)

**Framework**: CarKey  
**Kind**: method

Sends the specified custom data to the vehicle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
func sendPassthroughData(_ passthroughData: Data, toVehicle vehicleID: String) throws
```

#### Discussion

Use this method to send data that is custom to your specific vehicle. This method passes the data unmodified directly to the vehicle, and it is up to you to format the data exactly how the vehicle needs it.

If the vehicle sends a custom response, the system delivers it to the [`remoteControlSession(_:didReceivePassthroughData:fromVehicle:)`](carkeyremotecontrolsessiondelegate/remotecontrolsession(_:didreceivepassthroughdata:fromvehicle:).md) method of your session’s delegate object.

## Parameters

- `passthroughData`: The custom data to send to the vehicle. Make   sure the size of your data object doesn’t exceed 65 kilobytes.
- `vehicleID`: The target vehicle for the request. Choose the vehicle   from one of the session’s vehicle reports. Specify the string in the    property of the corresponding report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/sendpassthroughdata(_:tovehicle:))*