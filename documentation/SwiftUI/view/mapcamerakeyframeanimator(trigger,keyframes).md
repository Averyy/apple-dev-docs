# mapCameraKeyframeAnimator(trigger:keyframes:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapCameraKeyframeAnimator(trigger: some Equatable, @KeyframesBuilder<MapCamera> keyframes: @escaping (MapCamera) -> some Keyframes<MapCamera>) -> some View
```

## Discussion

When the trigger value changes, the map calls the `keyframes` closure to generate the keyframes that will animate the camera. The animation will continue for the duration of the keyframes that you specify.

If the user performs a gesture while the animation is in progress, the animation will be immediately removed, allowing the interaction to take control of the camera.

## Parameters

- `trigger`: A value to observe for changes.
- `keyframes`: A keyframes builder closure that is called when starting a new keyframe animation. The current map camera is provided as the only parameter.

## See Also

### Getting location information
- [struct LocationButton](../../CoreLocationUI/locationbutton.md)
  A SwiftUI button that grants one-time location authorization.
- [struct Map](../../MapKit/map.md)
  A view that displays an embedded map interface.
- [func mapStyle(MapStyle) -> some View](./mapstyle%28_%29.md)
  Specifies the map style to be used.
- [func mapScope(Namespace.ID) -> some View](./mapscope%28_%29.md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View](./mapfeatureselectiondisabled%28_%29.md)
  Specifies which map features should have selection disabled.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View](./mapfeatureselectionaccessory%28_%29.md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View](./mapfeatureselectioncontent%28content%29.md)
  Specifies a custom presentation for the currently selected feature.
- [func mapControls(() -> some View) -> some View](./mapcontrols%28_%29.md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func mapControlVisibility(Visibility) -> some View](./mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./lookaroundviewer%28ispresented,scene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./lookaroundviewer%28ispresented,initialscene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func onMapCameraChange(frequency:_:)](./onmapcamerachange%28frequency,_%29.md)
  Performs an action when Map camera framing changes
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](./mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor,arrowedge%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./mapitemdetailpopover%28item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mapcamerakeyframeanimator(trigger:keyframes:))*