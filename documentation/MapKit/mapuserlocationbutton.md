# MapUserLocationButton

**Framework**: MapKit  
**Kind**: struct

A button that sets the framing of the associated map to the user location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
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

You can also use `MapUserLocationButton` in conjunction with the [`mapControls(_:)`](https://developer.apple.com/documentation/swiftui/view/mapcontrols(_:)) modifier as shown in this example:

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
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View
](../swiftui/view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View
](../swiftui/view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func controlSize(_:)](../swiftui/view/controlsize(_:).md)
  Sets the size for controls within this view.
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View
](../swiftui/view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
### Setting the tint and border shape
- [func buttonBorderShape(ButtonBorderShape) -> some View
](../swiftui/view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func tint<S>(S) -> some MapContent](mapcontent/tint(_:).md)
  The tint shape style to apply to map content.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

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