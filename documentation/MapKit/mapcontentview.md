# MapContentView

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapContentView<SelectionValue, Content> where SelectionValue : Hashable, Content : MapContent
```

## Topics

### Managing feature selection
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View\n](../SwiftUI/view/mapfeatureselectioncontent%28content%29.md)
  Specifies a custom presentation for the currently selected feature.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View\n](../SwiftUI/view/mapfeatureselectiondisabled%28_%29.md)
  Specifies which map features should have selection disabled.
### Managing Look Around view presentation
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../SwiftUI/view/lookaroundviewer%28ispresented,initialscene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View
](../SwiftUI/view/lookaroundviewer%28ispresented,scene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
### Managing map control sizing and visibility
- [func mapControlVisibility(Visibility) -> some View\n](../SwiftUI/view/mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View\n](../SwiftUI/view/mapcontrols%28_%29.md)
  Configures all `Map` views in the associated environment to have standard size and position controls
### Managing the camera
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View\n](../SwiftUI/view/mapcamerakeyframeanimator%28trigger,keyframes%29.md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func onMapCameraChange(frequency: MapCameraUpdateFrequency, (MapCameraUpdateContext) -> Void) -> some View\n](../SwiftUI/view/onmapcamerachange%28frequency,_%29-2pcga.md)
  Performs an action when Map camera framing changes
- [func onMapCameraChange(frequency:_:)](../SwiftUI/view/onmapcamerachange%28frequency,_%29.md)
  Performs an action when Map camera framing changes
### Setting the visibility of the title and subtitle
- [func annotationTitles(Visibility) -> some MapContent](./mapcontent/annotationtitles%28_%29.md)
  Sets the visibility of titles for markers and annotations.
- [func annotationSubtitles(Visibility) -> some MapContent](./mapcontent/annotationsubtitles%28_%29.md)
  Sets the visibility of subtitles for markers and annotations.
### Setting the namespace Identifier
- [func mapScope(Namespace.ID) -> some View\n](../SwiftUI/view/mapscope%28_%29.md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
### Setting the map style
- [func mapStyle(MapStyle) -> some View\n](../SwiftUI/view/mapstyle%28_%29.md)
  Specifies the map style to be used.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Protocols
- [protocol DynamicMapContent](./dynamicmapcontent.md)
  A  type of view that generates views from an underlying collection of data.
- [protocol MapContent](./mapcontent.md)
  A protocol used to construct map content such as controls, markers, and annotations.
- [struct MapContentBuilder](./mapcontentbuilder.md)
  A result builder that creates map content from closures you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentview)*