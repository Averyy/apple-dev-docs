# init(item:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a marker for a given map item using a MapKit-provided label.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(item: MKMapItem) where Label == Text
```

## Discussion

MapKit composes a label using available information, such as the `name` property of `label`.

## Parameters

- `item`: An [`MKMapItem`](../mkmapitem.md) that provides a label for the marker.

## See Also

### Creating a marker
- [init<S>(S, coordinate: CLLocationCoordinate2D)](./init%28_,coordinate%29-82942.md)
  Creates a marker at the given location with the label you provide.
- [init<S>(S, image: String, coordinate: CLLocationCoordinate2D)](./init%28_,image,coordinate%29-36l1p.md)
  Creates a marker at the given location with the provided title and image resource to display as the balloon’s icon.
- [init<S>(S, systemImage: String, coordinate: CLLocationCoordinate2D)](./init%28_,systemimage,coordinate%29-50yl4.md)
  Creates a marker at the given location with the provided title and a system image the map displays as the balloon’s icon.
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D)](./init%28_,coordinate%29-8wxlv.md)
  Creates a marker at the given location with the localized string key you provide.
- [init(LocalizedStringKey, image: String, coordinate: CLLocationCoordinate2D)](./init%28_,image,coordinate%29-28mge.md)
  Creates a marker at the given location with the provided localized title and image resource to display as the balloon’s icon.
- [init(LocalizedStringKey, monogram: Text, coordinate: CLLocationCoordinate2D)](./init%28_,monogram,coordinate%29-2ojcy.md)
  Creates a marker at the given location with the provided title key and monogram.
- [init<S>(S, monogram: Text, coordinate: CLLocationCoordinate2D)](./init%28_,monogram,coordinate%29-21hql.md)
  Creates a marker at the given location with the provided title string and monogram.
- [init(LocalizedStringKey, systemImage: String, coordinate: CLLocationCoordinate2D)](./init%28_,systemimage,coordinate%29-2t4i0.md)
  Creates a marker at the given location with a localized title, and a system image the map displays as the balloon’s icon.
- [init(coordinate: CLLocationCoordinate2D, label: () -> Label)](./init%28coordinate,label%29.md)
  Creates a marker at the given location with the provided label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker/init(item:))*