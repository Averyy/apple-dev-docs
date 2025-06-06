# sign(data:forVehicle:)

**Framework**: CarKey  
**Kind**: method

Sign data with the endpoint.SK identified by vehicleIdentifier as described in the section “OEM App Data Attestation” of the Car Connectivity Consortium Digital Key Release 3.0 specification.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func sign(data: Data, forVehicle vehicleID: String) throws -> CarKeyRemoteControlSession.Attestation
```

#### Return Value

An Attestation object.

#### Discussion

This method can only be used while the application is in the foreground.

## Parameters

- `data`: The OEM App Data to sign.
- `vehicleID`: The vehicle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/sign(data:forvehicle:))*