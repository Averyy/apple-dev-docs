# Map

**Framework**: MapKit  
**Kind**: struct

A view that displays an embedded map interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Map<Content> where Content : View
```

#### Overview

Use this SwiftUI view to display a `Map` with markers, annotations, and custom content you provide. You can configure the `Map` to optionally display the user’s location, track a location, and display various controls to allow them to interact with and control the map’s display. The following example displays a map of downtown San Francisco that shows different markers, and an annotation with custom view content at specific locations:

```swift
    struct ContentView: View {
        var body: some View {
            Map {
                Marker("San Francisco City Hall", coordinate: cityHallLocation)
                    .tint(.orange)
                Marker("San Francisco Public Library", coordinate: publicLibraryLocation)
                    .tint(.blue)
                Annotation("Diller Civic Center Playground", coordinate: playgroundLocation) {
                    ZStack {
                        RoundedRectangle(cornerRadius: 5)
                            .fill(Color.yellow)
                        Text("🛝")
                            .padding(5)
                    }
                }
            }
            .mapControlVisibility(.hidden)
        }
    }
```

You create markers, annotations, and overlays using [`MapContentBuilder`](mapcontentbuilder.md) with any of several [`MapContent`](mapcontent.md) types including:

- [`Annotation`](annotation.md)
- [`UserAnnotation`](userannotation.md)
- [`Marker`](marker.md)
- [`MapCircle`](mapcircle.md)
- [`MapPolygon`](mappolygon.md)
- [`MapPolyline`](mappolyline.md)

You can also add a variety of controls to allow a person to interact with the map to change the map’s scale, display or hide the device’s current location, and so on:

- [`MapCompass`](mapcompass.md)
- [`MapPitchToggle`](mappitchtoggle.md)
- [`MapPitchSlider`](mappitchslider.md)
- [`MapScaleView`](mapscaleview.md)
- [`MapUserLocationButton`](mapuserlocationbutton.md)
- [`MapZoomStepper`](mapzoomstepper.md)

## Topics

### Creating a map
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:scope:content:).md)
  Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(bounds:interactionmodes:selection:scope:)-11lec.md)
  Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init<SelectedValue>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?)](map/init(bounds:interactionmodes:selection:scope:)-236di.md)
  Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:selection:scope:content:)-28wns.md)
  Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:selection:scope:content:)-2tdbr.md)
  Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(initialposition:bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:scope:content:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(initialposition:bounds:interactionmodes:selection:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-9feos.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-451vp.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(position:bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:scope:content:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(position:bounds:interactionmodes:selection:scope:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:selection:scope:content:)-47y4p.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
- [init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:selection:scope:content:)-9xq1q.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
- [struct MapInteractionModes](mapinteractionmodes.md)
  Options that indicate the user interactions that the map responds to.
### Managing feature selection
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View
](../SwiftUI/View/mapFeatureSelectionContent(content:).md)
  Specifies a custom presentation for the currently selected feature.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View
](../SwiftUI/View/mapFeatureSelectionDisabled(_:).md)
  Specifies which map features should have selection disabled.
### Managing Look Around view presentation
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../SwiftUI/View/lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:).md)
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../SwiftUI/View/lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:).md)
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View
](../SwiftUI/View/mapControlVisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View
](../SwiftUI/View/mapControls(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
### Managing the camera
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View
](../SwiftUI/View/mapCameraKeyframeAnimator(trigger:keyframes:).md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func onMapCameraChange(frequency: MapCameraUpdateFrequency, (MapCameraUpdateContext) -> Void) -> some View
](../SwiftUI/View/onMapCameraChange(frequency:_:)-2pcga.md)
  Performs an action when Map camera framing changes
- [func onMapCameraChange(frequency:_:)](../SwiftUI/View/onMapCameraChange(frequency:_:).md)
  Performs an action when Map camera framing changes
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View
](../SwiftUI/View/mapScope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
### Setting the map style
- [func mapStyle(MapStyle) -> some View
](../SwiftUI/View/mapStyle(_:).md)
  Specifies the map style to be used.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Map protocols and view modifiers that are no longer supported.
### Displaying place information
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View
](../SwiftUI/View/mapFeatureSelectionAccessory(_:).md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](mapcontent/mapitemdetailselectionaccessory(_:).md)
  Specifies the selection accessory to display for the selected map item content.
### Initializers
- [init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:selection:scope:content:)-335qt.md)
- [init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-2u4ry.md)
- [init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:selection:scope:content:)-96bhq.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct MapStyle](mapstyle.md)
  A style that you can apply to a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map)*