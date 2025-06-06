# MapAnnotation

**Framework**: MapKit  
**Kind**: struct

A customizable annotation that marks a map location.

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
struct MapAnnotation<Content> where Content : View
```

#### Overview

Use [`MapAnnotation`](mapannotation.md) to declare the layout of the view that MapKit uses for the annotation. Create a [`Map`](map.md) and display annotations by returning a view that conforms to [`MapAnnotationProtocol`](mapannotationprotocol.md) from the trailing closure of [`init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(coordinateregion:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md) or [`init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)`](map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:).md). Items you provide as a collection to the source  annotations need to conform to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable).

For example, the following code displays a map and a single annotation:

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

struct CustomAnnotationMapView: View {
    let place: IdentifiablePlace
    @State var region: MKCoordinateRegion

    var body: some View {
        Map(coordinateRegion: $region,
            annotationItems: [place]
        ) { place in
            MapAnnotation(coordinate: place.location) {
                Rectangle().stroke(Color.blue)
                .frame(width: 20, height: 20)
            }
        }
    }
}
```

## Topics

### Creating a map annotation
- [init(coordinate: CLLocationCoordinate2D, anchorPoint: CGPoint, content: () -> Content)](mapannotation/init(coordinate:anchorpoint:content:).md)
  Creates a custom annotation that provides a SwiftUI view to display at the map location that you specify.

## Relationships

### Conforms To
- [MapAnnotationProtocol](mapannotationprotocol.md)

## See Also

- [struct MapMarker](mapmarker.md)
  A balloon-shaped annotation used to indicate the location on a map.
- [struct MapPin](mappin.md)
  A pin-shaped annotation used to indicate a location on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapannotation)*