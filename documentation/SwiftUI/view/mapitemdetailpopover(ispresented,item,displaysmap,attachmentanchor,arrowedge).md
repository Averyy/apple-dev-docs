# mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a map item detail popover.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool = true, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge) -> some View
```

## Parameters

- `isPresented`: The binding to whether the detail sheet should be shown.
- `item`: The map item to display. If nil, a “loading” view is displayed.
- `displaysMap`: If an inline map should be displayed with the place data. A value of `true` must be specified if the application UI is not already showing the place in a map view.
- `attachmentAnchor`: The positioning anchor that defines the attachment point of the popover. The default is `bounds`.
- `arrowEdge`: The edge of the `attachmentAnchor` that defines the location of the popover’s arrow.

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
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](./mapcamerakeyframeanimator%28trigger,keyframes%29.md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./lookaroundviewer%28ispresented,scene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./lookaroundviewer%28ispresented,initialscene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func onMapCameraChange(frequency:_:)](./onmapcamerachange%28frequency,_%29.md)
  Performs an action when Map camera framing changes
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./mapitemdetailpopover%28item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:))*