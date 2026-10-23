# MapPitchSlider

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

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
- [init(scope: Namespace.ID?)](./mappitchslider/init%28scope%29.md)
  Creates a new map pitch slider with the scope you specify.
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View\n](../SwiftUI/view/mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View\n](../SwiftUI/view/mapcontrols%28_%29.md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func controlSize(_:)](../SwiftUI/view/controlsize%28_%29.md)
  Sets the size for controls within this view.
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View\n](../SwiftUI/view/mapscope%28_%29.md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Map controls
- [struct MapCompass](./mapcompass.md)
  A view that reflects the current orientation of the associated map.
- [struct MapLocationCompass](./maplocationcompass.md)
  A view that displays a combined user location button and map compass.
- [struct MapPitchToggle](./mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](./mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](./mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](./mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappitchslider)*