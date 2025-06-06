# init(bounds:interactionModes:scope:content:)

**Framework**: MapKit  
**Kind**: init

Creates a new map with the bounds, interaction modes, scope, and content you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init<C>(bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapContentView<Never, C>, C : MapContent
```

## Parameters

- `bounds`: The   that define the camera’s view of the map.
- `interactionModes`: The   that describe ways a person can interact with the map.
- `scope`: The map’s  .
- `content`: A   content builder that supplies the map’s content.

## See Also

- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the bounds, interaction modes, and scope you provide.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map/init(bounds:interactionmodes:scope:content:))*