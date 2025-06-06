# init(mapRect:interactionModes:showsUserLocation:userTrackingMode:)

**Framework**: MapKit  
**Kind**: init

Creates a map that displays a map rectangle and optionally configures available interactions, user location, and tracking behavior.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency init(mapRect: Binding<MKMapRect>, interactionModes: MapInteractionModes = .all, showsUserLocation: Bool = false, userTrackingMode: Binding<MapUserTrackingMode>? = nil) where Content == _DefaultMapContent
```

## Parameters

- `mapRect`: A binding to a rectangle on the map that corresponds to an area to display on the map.
- `interactionModes`: An enumeration that indicates the user interactions to which the map responds.
- `showsUserLocation`: A Boolean value that indicates the option to display a person’s location on a map. The map displays the location only if they authorized the app to access their location.
- `userTrackingMode`: A binding to a tracking mode that determines how the map responds to location updates.

## See Also

- [init(coordinateRegion: Binding<MKCoordinateRegion>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?)](map/init(coordinateregion:interactionmodes:showsuserlocation:usertrackingmode:).md)
  Creates a map that displays a coordinate region and optionally configures available interactions, user location, and tracking behavior.
- [init<Items, Annotation>(coordinateRegion: Binding<MKCoordinateRegion>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?, annotationItems: Items, annotationContent: (Items.Element) -> Annotation)](map/init(coordinateregion:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md)
  Creates a map that displays a coordinate region with annotations, and optionally configures available interactions, user location, and tracking behavior.
- [init<Items, Annotation>(mapRect: Binding<MKMapRect>, interactionModes: MapInteractionModes, showsUserLocation: Bool, userTrackingMode: Binding<MapUserTrackingMode>?, annotationItems: Items, annotationContent: (Items.Element) -> Annotation)](map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md)
  Creates a map that displays a map rectangle with annotations, and optionally configures available interactions, user location, and tracking behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:))*