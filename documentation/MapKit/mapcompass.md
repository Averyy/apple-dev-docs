# MapCompass

**Framework**: MapKit  
**Kind**: struct

A view that reflects the current orientation of the associated map.

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
@preconcurrency struct MapCompass
```

#### Overview

You can use `MapCompass` with a [`Map`](map.md) as a stand alone view, as shown in the following example:

```swift
    struct CompassButtonTestView: View {
        @Namespace var mapScope
        var body: some View {
        VStack {
                Map(scope: mapScope)
                MapCompass(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapCompass` with the `Map/mapControls(_:)`, modifier, as shown below:

```swift
    Map()
        .mapControls {
            MapCompass()
        }
```

Tapping the compass reorients the map so that North is at the top of the [`Map`](map.md) view.

## Topics

### Creating a map compass
- [init(scope: Namespace.ID?)](mapcompass/init(scope:).md)
  Creates a new map compass with the scope you specify.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct MapLocationCompass](maplocationcompass.md)
  A view that displays a combined user location button and map compass.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcompass)*