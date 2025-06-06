# MapPitchToggle

**Framework**: MapKit  
**Kind**: struct

A button that sets the pitch of the associated map.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct MapPitchToggle
```

#### Overview

The `MapPitchToggle` control sets the pitch of the associated map to a pleasing angle if flat, or returns the map to flat if pitched.

You can use this control in conjunction with [`Map`](map.md) as a standalone view, as this example shows:

```swift
    struct MyMapView: View {
        @Namespace var mapScope

        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapPitchToggle(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

Alternatively, use `MapPitchToggle` in conjunction with the `mapControls(_:)` modifier. For example:

```swift
    Map()
        .mapControls {
            MapPitchToggle()
        }
```

## Topics

### Creating a map pitch toggle
- [init(scope: Namespace.ID?)](mappitchtoggle/init(scope:).md)
  Creates a new map pitch toggle control with the provided scope.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct MapCompass](mapcompass.md)
  A view that reflects the current orientation of the associated map.
- [struct MapLocationCompass](maplocationcompass.md)
  A view that displays a combined user location button and map compass.
- [struct MapPitchSlider](mappitchslider.md)
  A slider control that allows a person to change the pitch of the map.
- [struct MapScaleView](mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappitchtoggle)*