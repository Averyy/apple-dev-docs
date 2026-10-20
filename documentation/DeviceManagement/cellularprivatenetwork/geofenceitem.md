# CellularPrivateNetwork.GeofenceItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A geofence for a private network.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```
object CellularPrivateNetwork.GeofenceItem
```

## Properties

- `GeofenceId` (string) *(required)*: A geofence identifier that’s unique within a list of geofences.
- `Latitude` (number) *(required)*: The latitude of the geofence.

  **Minimum**: `-90`; **Maximum**: `90`
- `Longitude` (number) *(required)*: The longitude of the geofence.

  **Minimum**: `-180`; **Maximum**: `180`
- `Radius` (number) *(required)*: Specifies the radius of the geofence in meters. Set this value slightly greater than the private cellular network coverage area.

  **Minimum**: `100`; **Maximum**: `6500`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellularprivatenetwork/geofenceitem)*