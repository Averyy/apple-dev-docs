# remoteControlSession(_:vehicleDidUpdateReport:)

**Framework**: CarKey  
**Kind**: method  
**Required**: Yes

Notifies your delegate object that the status of the specified vehicle changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
func remoteControlSession(_ session: CarKeyRemoteControlSession, vehicleDidUpdateReport: VehicleReport)
```

#### Discussion

When information for a vehicle changes, the session notifies its delegate so you can make any changes. To save time, use the provided report rather than requesting the report again from the session’s [`vehicleReports`](carkeyremotecontrolsession/vehiclereports.md) property. The system executes this method on the dispatch queue you specified when you started the session.

## Parameters

- `session`: The current session.
- `vehicleDidUpdateReport`: The updated vehicle report, which you   can use to make changes immediately.

## See Also

- [func remoteControlSession(CarKeyRemoteControlSession, didReceivePassthroughData: Data, fromVehicle: String)](carkeyremotecontrolsessiondelegate/remotecontrolsession(_:didreceivepassthroughdata:fromvehicle:).md)
  Notifies the delegate object that the vehicle sent passthrough data for you to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate/remotecontrolsession(_:vehicledidupdatereport:))*