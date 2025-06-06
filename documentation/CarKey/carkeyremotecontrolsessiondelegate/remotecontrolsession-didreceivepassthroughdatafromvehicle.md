# remoteControlSession(_:didReceivePassthroughData:fromVehicle:)

**Framework**: CarKey  
**Kind**: method  
**Required**: Yes

Notifies the delegate object that the vehicle sent passthrough data for you to handle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
func remoteControlSession(_ session: CarKeyRemoteControlSession, didReceivePassthroughData: Data, fromVehicle vehicleID: String)
```

#### Discussion

If the vehicle sends data, the system delivers it to your app using this method. You are responsible for the data your vehicles produce, and for decoding that data in your implementation of this method. The session doesn’t save or modify the data in any way.

The system executes this method on the dispatch queue you specified when you started the session.

## Parameters

- `session`: The current session.
- `didReceivePassthroughData`: The passthrough data that the vehicle   sent. Use the data to determine what actions to take, if any.
- `vehicleID`: The identifier of the vehicle that sent the data.   This identifier is the same string in the    property of the vehicle report.

## See Also

- [func remoteControlSession(CarKeyRemoteControlSession, vehicleDidUpdateReport: VehicleReport)](carkeyremotecontrolsessiondelegate/remotecontrolsession(_:vehicledidupdatereport:).md)
  Notifies your delegate object that the status of the specified vehicle changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate/remotecontrolsession(_:didreceivepassthroughdata:fromvehicle:))*