# remoteControlSession(_:didCreateKey:forVehicle:)

**Framework**: CarKey  
**Kind**: method  
**Required**: Yes

Called to notify your app when a new key has been created.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func remoteControlSession(_ session: CarKeyRemoteControlSession, didCreateKey keyID: String, forVehicle vehicleID: String)
```

## Parameters

- `session`: The current session.
- `keyID`: The identifier of the key.
- `vehicleID`: The identifier of the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate/remotecontrolsession(_:didcreatekey:forvehicle:))*