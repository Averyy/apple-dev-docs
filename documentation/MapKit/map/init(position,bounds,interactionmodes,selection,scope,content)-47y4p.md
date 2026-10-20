# init(position:bounds:interactionModes:selection:scope:content:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<MapFeature?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapContentView<MapFeature, C>, C : MapContent
```

Available when `Content` conforms to `View`.

## Parameters

- `position`: The initial [`MapCameraPosition`](../mapcameraposition.md).
- `bounds`: The [`MapCameraBounds`](../mapcamerabounds.md) that define the camera’s view of the map.
- `interactionModes`: The [`MapInteractionModes`](../mapinteractionmodes.md) that describe ways a person can interact with the map.
- `selection`: A binding to a [`MapFeature`](../mapfeature.md) that represents a person’s selection.
- `scope`: The map’s [`Namespace.ID`](../../SwiftUI/namespace/id.md).
- `content`: A [`MapContent`](../mapcontent.md) content builder that supplies the map’s content.

## See Also

### Creating a map
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./init%28bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./init%28bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./init%28bounds,interactionmodes,selection,scope%29-11lec.md)
  Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init<SelectedValue>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?)](./init%28bounds,interactionmodes,selection,scope%29-236di.md)
  Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](./init%28bounds,interactionmodes,selection,scope,content%29-28wns.md)
  Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](./init%28bounds,interactionmodes,selection,scope,content%29-2tdbr.md)
  Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./init%28initialposition,bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./init%28initialposition,bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./init%28initialposition,bounds,interactionmodes,selection,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](./init%28initialposition,bounds,interactionmodes,selection,scope,content%29-9feos.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](./init%28initialposition,bounds,interactionmodes,selection,scope,content%29-451vp.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./init%28position,bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./init%28position,bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./init%28position,bounds,interactionmodes,selection,scope%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](./init%28position,bounds,interactionmodes,selection,scope,content%29-9xq1q.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-47y4p)*