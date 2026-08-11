# MapPitchToggle

**Framework**: MapKit  
**Kind**: struct

A button that sets the pitch of the associated map.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
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

Alternatively, use `MapPitchToggle` in conjunction with the [`mapControls(_:)`](https://developer.apple.com/documentation/SwiftUI/View/mapControls(_:)) modifier. For example:

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
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View
](../SwiftUI/View/mapControlVisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View
](../SwiftUI/View/mapControls(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func controlSize(_:)](../SwiftUI/View/controlSize(_:).md)
  Sets the size for controls within this view.
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View
](../SwiftUI/View/mapScope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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