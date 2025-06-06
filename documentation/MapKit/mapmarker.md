# MapMarker

**Framework**: MapKit  
**Kind**: struct

A balloon-shaped annotation used to indicate the location on a map.

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
struct MapMarker
```

#### Overview

Create a [`Map`](map.md) and display marker annotations by returning a view that conforms to [`MapAnnotationProtocol`](mapannotationprotocol.md), such as [`MapMarker`](mapmarker.md), from the trailing closure of [`init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(coordinateregion:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md) or [`init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md). Items you provide as a collection to the source annotations need to conform to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable).

For example, the following code displays a map with a marker annotation:

```swift
struct IdentifiablePlace: Identifiable {
    let id: UUID
    let location: CLLocationCoordinate2D
    init(id: UUID = UUID(), lat: Double, long: Double) {
        self.id = id
        self.location = CLLocationCoordinate2D(
            latitude: lat,
            longitude: long)
    }
}

struct PinAnnotationMapView: View {
    let place: IdentifiablePlace
    @State var region: MKCoordinateRegion

    var body: some View {
        Map(coordinateRegion: $region,
            annotationItems: [place])
        { place in
            MapMarker(coordinate: place.location,
                   tint: Color.purple)
        }
    }
}

```

## Topics

### Creating a map marker
- [init(coordinate: CLLocationCoordinate2D, tint: Color?)](mapmarker/init(coordinate:tint:).md)
  Creates a marker annotation at the map location you specify.

## Relationships

### Conforms To
- [MapAnnotationProtocol](mapannotationprotocol.md)

## See Also

- [struct MapAnnotation](mapannotation.md)
  A customizable annotation that marks a map location.
- [struct MapPin](mappin.md)
  A pin-shaped annotation used to indicate a location on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapmarker)*