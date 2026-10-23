# MapLocationCompass

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

A view that displays a combined user location button and map compass.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapLocationCompass
```

#### Overview

In watchOS 10 and later, this view displays a combined [`MapUserLocationButton`](./mapuserlocationbutton.md) and [`MapCompass`](./mapcompass.md) control. When the map camera has a heading of zero (where north is up), this view shows the user location button. When the map camera is in a rotated state, it shows a compass.

Use `MapLocationCompass` in conjunction with [`Map`](./map.md) as a standalone view, as shown in this example:

```swift
    struct LocationCompassTestView: View {
        @Namespace var mapScope

        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapLocationCompass(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapLocationCompass` in conjunction with the [`mapControls(_:)`](../SwiftUI/view/mapcontrols%28_%29.md) modifier. For example:

```swift
    Map()
        .mapControls {
            MapLocationCompass()
        }
```

## Topics

### Creating a map loction compass
- [init(scope: Namespace.ID?)](./maplocationcompass/init%28scope%29.md)
  Creates a new map location compass with the provided scope.
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View\n](../SwiftUI/view/mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View\n](../SwiftUI/view/mapcontrols%28_%29.md)
  Configures all `Map` views in the associated environment to have standard size and position controls
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
- [struct MapPitchSlider](./mappitchslider.md)
  A slider control that allows a person to change the pitch of the map.
- [struct MapPitchToggle](./mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](./mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](./mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](./mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/maplocationcompass)*