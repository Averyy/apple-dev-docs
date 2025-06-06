# MapUserLocationButton

**Framework**: MapKit  
**Kind**: struct

A button that sets the framing of the associated map to the user location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapUserLocationButton
```

#### Overview

Use `MapUserLocationButton` in conjunction with [`Map`](map.md) as a stand alone view, as shown in this example:

```swift
    struct LocationButtonTestView: View {
        @Namespace var mapScope
        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapUserLocationButton(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapUserLocationButton` in conjunction with the `Map/mapControls(_:)` modifier as shown in this example:

```swift
    Map()
        .mapControls {
            MapUserLocationButton()
        }
```

## Topics

### Creating a map user location button
- [init(scope: Namespace.ID?)](mapuserlocationbutton/init(scope:).md)
  Creates a new user location button with the scope you specify.

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
- [struct MapPitchToggle](mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapuserlocationbutton)*