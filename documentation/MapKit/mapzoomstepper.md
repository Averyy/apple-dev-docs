# MapZoomStepper

**Framework**: MapKit  
**Kind**: struct

Buttons a person uses to adjust the zoom level of the map.

**Availability**:
- Mac Catalyst 14.0+
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapZoomStepper
```

#### Overview

You typically use [`MapZoomStepper`](mapzoomstepper.md) with [`Map`](map.md) as a stand alone view, as shown in the following example:

```swift
    struct ZoomStepperTestView: View {
        @Namespace var mapScope
        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapZoomStepper(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use a MapZoomStepper in conjunction with the [`mapControls(_:)`](https://developer.apple.com/documentation/swiftui/view/mapcontrols(_:)) modifier, as show in here:

```swift
    Map()
        .mapControls {
            MapZoomStepper()
        }
```

## Topics

### Creating a zoom stepper
- [init(scope: Namespace.ID?)](mapzoomstepper/init(scope:).md)
  Creates a new zoom stepper with the scope you specify.
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View
](../swiftui/view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View
](../swiftui/view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func controlSize(_:)](../swiftui/view/controlsize(_:).md)
  Sets the size for controls within this view.
### Setting the namespace identifier
- [func mapScope(Namespace.ID) -> some View
](../swiftui/view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.

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
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapzoomstepper)*