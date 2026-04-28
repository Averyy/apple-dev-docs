# CellularPrivateNetwork.GeofenceItem

**Framework**: Device Management  
**Kind**: dictionary

A geofence for a private network.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object CellularPrivateNetwork.GeofenceItem
```

## Properties

- `GeofenceId` (string) *(required)*: A geofence identifier that’s unique within a list of geofences.
- `Latitude` (number) *(required)*: The latitude of the geofence.
- `Longitude` (number) *(required)*: The longitude of the geofence.
- `Radius` (number) *(required)*: Specifies the radius of the geofence in meters. Set this value slightly greater than the private cellular network coverage area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellularprivatenetwork/geofenceitem)*