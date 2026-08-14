# MapReader

**Framework**: MapKit  
**Kind**: struct

A container view that defines its contents as a function of information about the first contained map.

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
@preconcurrency struct MapReader<Content> where Content : View
```

#### Overview

The map reader’s content builder receives a [`MapProxy`](mapproxy.md) instance. You can use this instance to get the information you’ll need to convert between a [`MapCamera`](mapcamera.md) and a [`MKMapRect`](mkmaprect.md) or [`MKCoordinateRegion`](mkcoordinateregion.md).

## Topics

### Creating a map reader
- [init(content: (MapProxy) -> Content)](mapreader/init(content:).md)
  Creates an instance that allows view content to reference information about a contained map.
### Managing Look Around view presentation
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../swiftui/view/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../swiftui/view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
### Managing map controls
- [func mapControlVisibility(Visibility) -> some View
](../swiftui/view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View
](../swiftui/view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
### Managing the camera
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View
](../swiftui/view/mapcamerakeyframeanimator(trigger:keyframes:).md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func onMapCameraChange(frequency: MapCameraUpdateFrequency, (MapCameraUpdateContext) -> Void) -> some View
](../swiftui/view/onmapcamerachange(frequency:_:)-2pcga.md)
  Performs an action when Map camera framing changes
- [func onMapCameraChange(frequency:_:)](../swiftui/view/onmapcamerachange(frequency:_:).md)
  Performs an action when Map camera framing changes
### Managing feature selection
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View
](../swiftui/view/mapfeatureselectioncontent(content:).md)
  Specifies a custom presentation for the currently selected feature.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View
](../swiftui/view/mapfeatureselectiondisabled(_:).md)
  Specifies which map features should have selection disabled.
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View
](../swiftui/view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
### Setting the map style
- [func mapStyle(MapStyle) -> some View
](../swiftui/view/mapstyle(_:).md)
  Specifies the map style to be used.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

## See Also

- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapProxy](mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapreader)*