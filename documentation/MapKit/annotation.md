# Annotation

**Framework**: MapKit  
**Kind**: struct

A customizable annotation used to indicate a location on a map.

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
@preconcurrency struct Annotation<Label, Content> where Label : View, Content : View
```

#### Overview

Use this view to annotations in the closure you provide to the `content` parameter in the [`Map`](map.md) initializers.

## Topics

### Creating annotations
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:accessoryanchor:content:)-6rxmn.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:accessoryanchor:content:)-14m3t.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content, label: () -> Label)](annotation/init(coordinate:anchor:accessoryanchor:content:label:).md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(item: MKMapItem, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(item:anchor:accessoryanchor:content:).md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:content:)-2w242.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:content:)-6wnoh.md)
  Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content, label: () -> Label)](annotation/init(coordinate:anchor:content:label:).md)
  Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.
### Setting the visibility of the title and subtitle
- [func annotationTitles(Visibility) -> some MapContent](mapcontent/annotationtitles(_:).md)
  Sets the visibility of titles for markers and annotations.
- [func annotationSubtitles(Visibility) -> some MapContent](mapcontent/annotationsubtitles(_:).md)
  Sets the visibility of subtitles for markers and annotations.
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
- [init(LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:accessoryanchor:content:)-8wi4r.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:content:)-8k419.md)
  Creates an annotation that displays a view at a coordinate on the map.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/annotation)*