# MapPin

**Framework**: MapKit  
**Kind**: struct

A pin-shaped annotation used to indicate a location on a map.

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
struct MapPin
```

#### Overview

Create a [`Map`](map.md) and display pin annotations by returning a view that conforms to [`MapAnnotationProtocol`](mapannotationprotocol.md), such as [`MapPin`](mappin.md), from the trailing closure of [`init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(coordinateregion:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md) or [`init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md). Items you provide as a collection to the source annotations need to conform to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable).

For example, the following code displays a map with a pin annotation:

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
            MapPin(coordinate: place.location,
                   tint: Color.purple)
        }
    }
}
```

## Topics

### Creating a map pin
- [init(coordinate: CLLocationCoordinate2D, tint: Color?)](mappin/init(coordinate:tint:).md)
  Creates a map pin at the map location that you specify.

## Relationships

### Conforms To
- [MapAnnotationProtocol](mapannotationprotocol.md)

## See Also

- [struct MapAnnotation](mapannotation.md)
  A customizable annotation that marks a map location.
- [struct MapMarker](mapmarker.md)
  A balloon-shaped annotation used to indicate the location on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappin)*