# mapControls(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures all `Map` views in the associated environment to have standard size and position controls

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
@preconcurrency func mapControls(@ViewBuilder _ content: () -> some View) -> some View
```

#### Discussion

You provide the controls you want to appear atop your map. When using a control in conjunction with `.mapControls` you don’t need to specify a scope. Views that are not MapKit controls will be ignored.

```swift
Map()
.mapControls {
    MapScaleView()
    MapUserLocationButton()
}
```

Controls can be modified individually or all at once. Custom frames and alignments set on controls are ignored.

```swift
Map()
.mapControls {
    MapCompass()
        .mapControls(.visible)
    MapPitchToggle()
        .buttonBorderShape(.circular)
        .tint(.purple)
}
.controlSize(.large)
```

On watchOS, space is at a premium. When using the mapControls modifier, MapUserLocationButton and MapCompass are automatically combined if present.

```swift
Map()
.mapControls {
    MapUserLocationButton()
    MapCompass()
}
```

## Parameters

- `content`: A view builder returning the controls you wish your `Map`

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
- [func mapControlVisibility(Visibility) -> some View](./mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](./mapcamerakeyframeanimator%28trigger,keyframes%29.md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mapcontrols(_:))*