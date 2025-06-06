# init(_:coordinate:)

**Framework**: MapKit  
**Kind**: init

Creates a marker at the given location with the localized string key you provide.

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
@preconcurrency init(_ titleKey: LocalizedStringKey, coordinate: CLLocationCoordinate2D) where Label == Text
```

## Parameters

- `titleKey`: The localized string key to use to lookup the title.
- `coordinate`: The coordinate used to display the marker.

## See Also

- [init<S>(S, coordinate: CLLocationCoordinate2D)](marker/init(_:coordinate:)-82942.md)
  Creates a marker at the given location with the label you provide.
- [init<S>(S, image: String, coordinate: CLLocationCoordinate2D)](marker/init(_:image:coordinate:)-36l1p.md)
  Creates a marker at the given location with the provided title and image resource to display as the balloon’s icon.
- [init<S>(S, systemImage: String, coordinate: CLLocationCoordinate2D)](marker/init(_:systemimage:coordinate:)-50yl4.md)
  Creates a marker at the given location with the provided title and a system image the map displays as the balloon’s icon.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker/init(_:coordinate:)-8wxlv)*