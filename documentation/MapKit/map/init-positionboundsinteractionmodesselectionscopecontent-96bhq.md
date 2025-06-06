# init(position:bounds:interactionModes:selection:scope:content:)

**Framework**: MapKit  
**Kind**: init

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<SelectedValue?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapSelectableContentView<SelectedValue, C>, SelectedValue : MapSelectable, C : MapContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-96bhq)*