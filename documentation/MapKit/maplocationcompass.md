# MapLocationCompass

**Framework**: MapKit  
**Kind**: struct

A view that displays a combined user location button and map compass.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapLocationCompass
```

#### Overview

In watchOS 10 and later, this view displays a combined [`MapUserLocationButton`](mapuserlocationbutton.md) and [`MapCompass`](mapcompass.md) control. When the map camera has a heading of zero (where north is up), this view shows the user location button. When the map camera is in a rotated state, it shows a compass.

Use `MapLocationCompass` in conjunction with [`Map`](map.md) as a standalone view, as shown in this example:

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

You can also use `MapLocationCompass` in conjunction with the `mapControls(_:)` modifier. For example:

```swift
    Map()
        .mapControls {
            MapLocationCompass()
        }
```

## Topics

### Creating a map loction compass
- [init(scope: Namespace.ID?)](maplocationcompass/init(scope:).md)
  Creates a new map location compass with the provided scope.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct MapCompass](mapcompass.md)
  A view that reflects the current orientation of the associated map.
- [struct MapPitchSlider](mappitchslider.md)
  A slider control that allows a person to change the pitch of the map.
- [struct MapPitchToggle](mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/maplocationcompass)*