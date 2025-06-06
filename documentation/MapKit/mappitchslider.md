# MapPitchSlider

**Framework**: MapKit  
**Kind**: struct

A slider control that allows a person to change the pitch of the map.

**Availability**:
- Mac Catalyst 14.0+
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapPitchSlider
```

## Topics

### Creating a map pitch slider
- [init(scope: Namespace.ID?)](mappitchslider/init(scope:).md)
  Creates a new map pitch slider with the scope you specify.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct MapCompass](mapcompass.md)
  A view that reflects the current orientation of the associated map.
- [struct MapLocationCompass](maplocationcompass.md)
  A view that displays a combined user location button and map compass.
- [struct MapPitchToggle](mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappitchslider)*