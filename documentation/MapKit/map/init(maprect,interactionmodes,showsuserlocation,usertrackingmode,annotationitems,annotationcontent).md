# init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a map that displays a map rectangle with annotations, and optionally configures available interactions, user location, and tracking behavior.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use [`Map`](../map.md) initializers that take a [`MapContentBuilder`](../mapcontentbuilder.md) instead.

## Declaration

```swift
@MainActor
@preconcurrency init<Items, Annotation>(mapRect: Binding<MKMapRect>, interactionModes: MapInteractionModes = .all, showsUserLocation: Bool = false, userTrackingMode: Binding<MapUserTrackingMode>? = nil, annotationItems: Items, annotationContent: @escaping (Items.Element) -> Annotation) where Content == _DefaultAnnotatedMapContent<Items>, Items : RandomAccessCollection, Annotation : MapAnnotationProtocol, Items.Element : Identifiable
```

## Parameters

- `mapRect`: The map rectangle defining the area to display.
- `interactionModes`: An enumeration that indicates the user interactions to which the map responds.
- `showsUserLocation`: A Boolean value that indicates the option to display a person’s location on a map. The map displays the location only if they authorized the app to access their location.
- `userTrackingMode`: A binding to a tracking mode that determines how the map responds to location updates.
- `annotationItems`: The collection of data that the view uses to display annotations.
- `annotationContent`: A closure that produces the annotation content.

## See Also

### Initializers
- [init(coordinateRegion: Binding<MKCoordinateRegion>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?)](./init%28coordinateregion,interactionmodes,showsuserlocation,usertrackingmode%29.md)
  Creates a map that displays a coordinate region and optionally configures available interactions, user location, and tracking behavior.
- [init<Items, Annotation>(coordinateRegion: Binding<MKCoordinateRegion>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?, annotationItems: Items, annotationContent: (Items.Element) -> Annotation)](./init%28coordinateregion,interactionmodes,showsuserlocation,usertrackingmode,annotationitems,annotationcontent%29.md)
  Creates a map that displays a coordinate region with annotations, and optionally configures available interactions, user location, and tracking behavior.
- [init(mapRect: Binding<MKMapRect>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?)](./init%28maprect,interactionmodes,showsuserlocation,usertrackingmode%29.md)
  Creates a map that displays a map rectangle and optionally configures available interactions, user location, and tracking behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:))*