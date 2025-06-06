# MapScaleView

**Framework**: MapKit  
**Kind**: struct

Displays a legend with distance information for the associated map.

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
@preconcurrency struct MapScaleView
```

#### Overview

You can use this with [`Map`](map.md) as a standalone view, for example:

```swift
    struct ScaleTestView: View {
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

The scale indicator grows and shrinks (although visually, its frame is static) based on the zoom level of the map. By default the leading edge remains anchored and the trailing edge moves as the scale changes. If the scale is trailing aligned, then it may be more visually appealing to anchor the `ScaleView` to the trailing edge

```swift
    ZStack(alignment: .trailing) {
        Map(mapScope)
        MapScaleView(anchorEdge: .trailing, scope: mapScope)
    }
    .mapScope(mapScope)
```

You can also use `MapScaleView` with the [`mapControls(_:)`](https://developer.apple.com/documentation/SwiftUI/View/mapControls(_:)) modifier, as shown in this example:

```swift
    Map()
        .mapControls {
            MapScaleView()
        }
```

## Topics

### Creating a map scale view
- [init(anchorEdge: HorizontalEdge, scope: Namespace.ID?)](mapscaleview/init(anchoredge:scope:).md)
  Creates a map scale view.

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
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapscaleview)*