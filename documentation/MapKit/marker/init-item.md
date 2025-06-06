# init(item:)

**Framework**: MapKit  
**Kind**: init

Creates a marker for a given map item using a MapKit-provided label.

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
@preconcurrency init(item: MKMapItem) where Label == Text
```

#### Discussion

MapKit composes a label using available information, such as the `name` property of `label`.

## Parameters

- `item`: An   that provides a label for the marker.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker/init(item:))*