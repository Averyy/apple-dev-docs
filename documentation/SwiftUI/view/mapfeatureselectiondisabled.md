# mapFeatureSelectionDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies which map features should have selection disabled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapFeatureSelectionDisabled(_ selectionDisabled: @escaping (MapFeature) -> Bool) -> some View
```

#### Discussion

The `selectionDisabled` parameter takes a closure which maps map features, to booleans. If that closure returns true for a given map feature, that map feature will be considered unselectable.

## Parameters

- `selectionDisabled`: Determines if selection should be disabled for a given   map feature.

## See Also

- [@MainActor @preconcurrency struct LocationButton](../CoreLocationUI/LocationButton.md)
  A SwiftUI button that grants one-time location authorization.
- [@MainActor @preconcurrency struct Map<Content> where Content : View](../MapKit/Map.md)
  A view that displays an embedded map interface.
- [func mapStyle(MapStyle) -> some View](view/mapstyle(_:).md)
  Specifies the map style to be used.
- [func mapScope(Namespace.ID) -> some View](view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View](view/mapfeatureselectionaccessory(_:).md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View](view/mapfeatureselectioncontent(content:).md)
  Specifies a custom presentation for the currently selected feature.
- [func mapControls(() -> some View) -> some View](view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func mapControlVisibility(Visibility) -> some View](view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](view/mapcamerakeyframeanimator(trigger:keyframes:).md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func onMapCameraChange(frequency:_:)](view/onmapcamerachange(frequency:_:).md)
  Performs an action when Map camera framing changes
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mapfeatureselectiondisabled(_:))*