# Marker

**Framework**: MapKit  
**Kind**: struct

A balloon-shaped annotation that marks a map location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Marker<Label> where Label : View
```

#### Overview

Use this view to create marker instances in the closure you provide to the `content` parameter in the [`Map`](map.md) initializers.

## Topics

### Creating a marker
- [init<S>(S, coordinate: CLLocationCoordinate2D)](marker/init(_:coordinate:)-82942.md)
  Creates a marker at the given location with the label you provide.
- [init<S>(S, image: String, coordinate: CLLocationCoordinate2D)](marker/init(_:image:coordinate:)-36l1p.md)
  Creates a marker at the given location with the provided title and image resource to display as the balloon’s icon.
- [init<S>(S, systemImage: String, coordinate: CLLocationCoordinate2D)](marker/init(_:systemimage:coordinate:)-50yl4.md)
  Creates a marker at the given location with the provided title and a system image the map displays as the balloon’s icon.
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D)](marker/init(_:coordinate:)-8wxlv.md)
  Creates a marker at the given location with the localized string key you provide.
- [init(LocalizedStringKey, image: String, coordinate: CLLocationCoordinate2D)](marker/init(_:image:coordinate:)-28mge.md)
  Creates a marker at the given location with the provided localized title and image resource to display as the balloon’s icon.
- [init(LocalizedStringKey, monogram: Text, coordinate: CLLocationCoordinate2D)](marker/init(_:monogram:coordinate:)-2ojcy.md)
  Creates a marker at the given location with the provided title key and monogram.
- [init<S>(S, monogram: Text, coordinate: CLLocationCoordinate2D)](marker/init(_:monogram:coordinate:)-21hql.md)
  Creates a marker at the given location with the provided title string and monogram.
- [init(LocalizedStringKey, systemImage: String, coordinate: CLLocationCoordinate2D)](marker/init(_:systemimage:coordinate:)-2t4i0.md)
  Creates a marker at the given location with a localized title, and a system image the map displays as the balloon’s icon.
- [init(coordinate: CLLocationCoordinate2D, label: () -> Label)](marker/init(coordinate:label:).md)
  Creates a marker at the given location with the provided label.
- [init(item: MKMapItem)](marker/init(item:).md)
  Creates a marker for a given map item using a MapKit-provided label.
### Setting the visibility of the title and subtitle
- [func annotationTitles(Visibility) -> some MapContent](mapcontent/annotationtitles(_:).md)
  Sets the visibility of titles for markers and annotations.
- [func annotationSubtitles(Visibility) -> some MapContent](mapcontent/annotationsubtitles(_:).md)
  Sets the visibility of subtitles for markers and annotations.
### Styling the marker
- [func tint<S>(S) -> some MapContent](mapcontent/tint(_:).md)
  The tint shape style to apply to map content.
### Setting the tag
- [func tag<V>(V) -> some MapContent](mapcontent/tag(_:).md)
  Sets the unique tag value of this piece of map content.
### Type aliases
- [associatedtype Body : MapContent](mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.
### Displaying place information
- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](mapcontent/mapitemdetailselectionaccessory(_:).md)
  Specifies the selection accessory to display for the selected map item content.
### Initializers
- [init(LocalizedStringResource, coordinate: CLLocationCoordinate2D)](marker/init(_:coordinate:)-3bjj6.md)
  Creates a marker at the given location.
- [init(LocalizedStringResource, image: String, coordinate: CLLocationCoordinate2D)](marker/init(_:image:coordinate:)-1q3pz.md)
  Creates a marker at the given location with an image displayed as the balloon’s icon.
- [init(LocalizedStringResource, monogram: Text, coordinate: CLLocationCoordinate2D)](marker/init(_:monogram:coordinate:)-77k4r.md)
  Creates a marker at the given location with a monogram displayed as the balloon’s icon.
- [init(LocalizedStringResource, systemImage: String, coordinate: CLLocationCoordinate2D)](marker/init(_:systemimage:coordinate:)-18xnl.md)
  Creates a marker at the given location with a system image displayed as the balloon’s icon.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker)*